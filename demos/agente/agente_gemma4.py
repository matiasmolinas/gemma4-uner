"""
Agente mínimo con function calling nativo sobre Gemma 4, corriendo local en Ollama.

El punto pedagógico: el modelo decide QUÉ herramienta llamar y EN QUÉ ORDEN.
No hay un if/else que enrute. El loop de abajo solo ejecuta lo que el modelo pide.

Uso:
    ollama pull gemma4:e4b
    pip install ollama
    python agente_gemma4.py

Escenario: inventario de laboratorio. Tres herramientas:
  - buscar_reactivo(nombre)      -> consulta el "inventario"
  - dias_hasta_vencimiento(fecha)-> aritmética de fechas (los LLM son malos en esto)
  - registrar_pedido(catalogo, cantidad) -> acción con efecto

Prompt de prueba que fuerza multi-paso:
    "¿Nos queda cloruro de sodio? Si vence en menos de 90 días, pedí 2 más."

El modelo tiene que: buscar -> calcular días -> decidir -> pedir.
Cuatro pasos. Ninguno está codificado.
"""

import json
from datetime import date, datetime

import ollama

# ---------------------------------------------------------------------------
# NOTA DE VERSIÓN (leer antes de la charla)
# ---------------------------------------------------------------------------
# El tag exacto del modelo cambió entre releases. Verificá con:
#     ollama list
# y ajustá MODELO. Candidatos vistos en la documentación: "gemma4",
# "gemma4:e4b", "gemma4:12b".
MODELO = "gemma4:e4b"


# ---------------------------------------------------------------------------
# "Base de datos" del laboratorio. En un proyecto real esto es Postgres.
# ---------------------------------------------------------------------------
INVENTARIO = {
    "cloruro de sodio": {
        "catalogo": "S9888-500G",
        "producto": "Sodium Chloride, ACS reagent, >=99.0%",
        "stock": 1,
        "vencimiento": "2026-09-15",
    },
    "etanol absoluto": {
        "catalogo": "E7023-500ML",
        "producto": "Ethanol, absolute, >=99.8%",
        "stock": 4,
        "vencimiento": "2027-02-28",
    },
    "agarosa": {
        "catalogo": "A9539-25G",
        "producto": "Agarose, low EEO",
        "stock": 0,
        "vencimiento": "2028-11-30",
    },
}

PEDIDOS = []


# ---------------------------------------------------------------------------
# Herramientas. Funciones normales de Python. Nada especial.
# ---------------------------------------------------------------------------
def buscar_reactivo(nombre: str) -> str:
    """Busca un reactivo en el inventario del laboratorio."""
    clave = nombre.strip().lower()
    for k, v in INVENTARIO.items():
        if clave in k or k in clave:
            return json.dumps({"encontrado": True, **v}, ensure_ascii=False)
    return json.dumps(
        {"encontrado": False, "disponibles": list(INVENTARIO)}, ensure_ascii=False
    )


def dias_hasta_vencimiento(fecha: str) -> str:
    """Días entre hoy y una fecha en formato YYYY-MM-DD. Negativo si ya venció."""
    try:
        objetivo = datetime.strptime(fecha.strip(), "%Y-%m-%d").date()
    except ValueError:
        return json.dumps({"error": "formato_invalido", "esperado": "YYYY-MM-DD"})
    return json.dumps({"dias": (objetivo - date.today()).days, "fecha": fecha})


def registrar_pedido(catalogo: str, cantidad: int) -> str:
    """Registra un pedido de compra. Acción con efecto: modifica estado."""
    cantidad = int(cantidad)
    if cantidad <= 0:
        return json.dumps({"error": "cantidad_debe_ser_positiva"})
    PEDIDOS.append({"catalogo": catalogo, "cantidad": cantidad})
    return json.dumps(
        {"ok": True, "catalogo": catalogo, "cantidad": cantidad, "total_pedidos": len(PEDIDOS)}
    )


TOOLS_IMPL = {
    "buscar_reactivo": buscar_reactivo,
    "dias_hasta_vencimiento": dias_hasta_vencimiento,
    "registrar_pedido": registrar_pedido,
}

# Las declaraciones que ve el modelo. La `description` es lo que decide
# si la tool se usa o no: escribila para el modelo, no para el humano.
TOOLS_SPEC = [
    {
        "type": "function",
        "function": {
            "name": "buscar_reactivo",
            "description": (
                "Busca un reactivo o insumo en el inventario del laboratorio. "
                "Devuelve número de catálogo, stock actual y fecha de vencimiento."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre": {
                        "type": "string",
                        "description": "Nombre común del reactivo, ej: 'cloruro de sodio'",
                    }
                },
                "required": ["nombre"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "dias_hasta_vencimiento",
            "description": (
                "Calcula cuántos días faltan hasta una fecha de vencimiento. "
                "Usala SIEMPRE en vez de calcular fechas mentalmente."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "fecha": {"type": "string", "description": "Fecha en formato YYYY-MM-DD"}
                },
                "required": ["fecha"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "registrar_pedido",
            "description": (
                "Registra un pedido de compra de un insumo. Es una ACCIÓN con efecto: "
                "usala solo cuando el usuario lo pidió explícitamente o cuando una "
                "condición que él definió se cumple."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "catalogo": {"type": "string", "description": "Número de catálogo del producto"},
                    "cantidad": {"type": "integer", "description": "Unidades a pedir"},
                },
                "required": ["catalogo", "cantidad"],
            },
        },
    },
]

SYSTEM = (
    "Sos un asistente de inventario de un laboratorio de bioingeniería. "
    "Usás las herramientas disponibles para responder con datos reales; nunca "
    "inventás stock, catálogos ni fechas. Para cualquier cálculo de fechas usás "
    "la herramienta, no tu propia aritmética. Respondés en español rioplatense, breve."
)


def correr(pregunta: str, max_pasos: int = 8, verbose: bool = True) -> str:
    """Loop de agente. Ejecuta lo que el modelo pide, hasta que deja de pedir."""
    mensajes = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": pregunta},
    ]

    for paso in range(max_pasos):
        resp = ollama.chat(model=MODELO, messages=mensajes, tools=TOOLS_SPEC)
        msg = resp["message"]
        mensajes.append(msg)

        llamadas = msg.get("tool_calls") or []
        if not llamadas:
            return msg.get("content", "")

        for llamada in llamadas:
            fn = llamada["function"]["name"]
            args = llamada["function"].get("arguments", {}) or {}
            if isinstance(args, str):  # algunos runtimes devuelven el JSON como string
                args = json.loads(args)

            if verbose:
                print(f"  [paso {paso + 1}] el modelo llama: {fn}({args})")

            impl = TOOLS_IMPL.get(fn)
            resultado = (
                impl(**args) if impl else json.dumps({"error": f"tool_desconocida:{fn}"})
            )

            if verbose:
                print(f"           -> {resultado}")

            # OJO: Gemma 4 usa el rol "model" para el asistente, pero el rol de
            # los resultados de herramienta sigue siendo "tool".
            mensajes.append({"role": "tool", "name": fn, "content": resultado})

    return "(se agotaron los pasos sin respuesta final)"


if __name__ == "__main__":
    pruebas = [
        # 1 sola tool
        "¿Tenemos agarosa?",
        # multi-paso: buscar -> calcular -> decidir -> actuar
        "¿Nos queda cloruro de sodio? Si vence en menos de 90 días, pedí 2 más.",
        # el modelo NO debería llamar ninguna tool acá
        "¿Qué es un pictograma GHS?",
    ]

    for p in pruebas:
        print("\n" + "=" * 72)
        print(f"USUARIO: {p}\n")
        print(f"AGENTE:  {correr(p)}")

    print("\n" + "=" * 72)
    print(f"Pedidos registrados: {PEDIDOS}")
