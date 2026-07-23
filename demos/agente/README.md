# Agente con function calling nativo

Un agente mínimo sobre Gemma 4 local: tres herramientas de inventario de
laboratorio, y **ningún `if/else` que enrute**. El modelo decide qué herramienta
llamar y en qué orden. El loop solo ejecuta lo que el modelo pide.

Usalo como esqueleto para cualquier proyecto de agente del hackathon.

## Setup y correr

```bash
ollama pull gemma4:e4b
pip install -r requirements.txt
python agente_gemma4.py
```

## Qué demuestra

El prompt clave fuerza **cuatro pasos autónomos**:

> *"¿Nos queda cloruro de sodio? Si vence en menos de 90 días, pedí 2 más."*

buscar → calcular días → decidir → registrar el pedido. Ninguno está codificado.

Y la tercera prueba (*"¿qué es un pictograma GHS?"*) demuestra lo contrario:
el modelo **no llama ninguna herramienta** cuando la pregunta es conceptual.
Saber cuándo *no* usar una tool es tan importante como saber cuándo usarla.

**Verificado (jul-2026, `gemma4:e4b`, MacBook M4):** las tres pruebas pasan;
la cadena completa tarda ~70 s.

## Los dos gotchas que te van a costar horas

**1. El rol del asistente es `model`, no `assistant`** — pero los resultados de
herramienta siguen usando el rol `tool`. Es una asimetría que confunde, y en
fine-tuning es silenciosa y letal (ver notebook 02).

**2. En vLLM, `enable_thinking` prende razonamiento Y function calling a la vez.**
Están acoplados. Si tu agente no llama tools, chequeá esto antes de culpar al modelo:

```python
extra_body={"chat_template_kwargs": {"enable_thinking": True}}
```

Con Docker Model Runner hay reportes de que hace falta el shim
`GemmaFunctionCallingMixin` del ADK.

## Qué tamaño usar para agentes (contraintuitivo)

- **E4B es el sweet spot**: ~22 s las consultas simples, ~2,5 min las complejas.
- **26B / 31B son demasiado lentos** para loops multi-roundtrip: la latencia se
  multiplica por cada ida y vuelta.

El viernes a la noche vas a querer el 31B "porque es mejor". No lo es. Para
esto, no.

## Para tu proyecto

- Las `description` de las tools son lo que decide si el modelo las usa:
  escribilas **para el modelo**, no para el humano que lee el código.
- La herramienta de fechas existe porque los LLM son malos en aritmética de
  calendario. Identificá qué cálculos tu agente NO debe hacer "de cabeza".
- `registrar_pedido` es una acción con efecto: fijate cómo la description le
  exige al modelo una condición explícita antes de usarla.
