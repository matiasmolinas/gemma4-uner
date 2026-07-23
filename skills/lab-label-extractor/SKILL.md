---
name: lab-label-extractor
description: Extrae datos estructurados de la foto de una etiqueta de un reactivo, frasco, vial o insumo de laboratorio. Se activa cuando el usuario adjunta la imagen de una etiqueta, envase, rótulo o packaging de laboratorio, o cuando pide "cargar", "digitalizar", "leer" o "pasar a JSON" una etiqueta, un reactivo o un insumo. También se activa ante fotos de códigos de lote, fechas de vencimiento o números de catálogo de productos de laboratorio.
license: Apache-2.0
---

# Extractor de etiquetas de laboratorio

Convertís la foto de una etiqueta de laboratorio en un registro JSON limpio, listo para cargar en un inventario.

## Tu tarea

Cuando recibas la imagen de una etiqueta de laboratorio, extraé los campos que están abajo y devolvé **únicamente** un objeto JSON. Sin preámbulo, sin explicación, sin bloques de código markdown.

## Esquema de salida

```json
{
  "producto": "string",
  "fabricante": "string | null",
  "numero_catalogo": "string | null",
  "lote": "string | null",
  "cantidad": { "valor": number, "unidad": "string" } | null,
  "concentracion": { "valor": number, "unidad": "string" } | null,
  "fecha_vencimiento": "YYYY-MM-DD | null",
  "temperatura_almacenamiento": "string | null",
  "pictogramas_ghs": ["string"],
  "cas": "string | null",
  "confianza": "alta | media | baja",
  "campos_ilegibles": ["string"]
}
```

## Ejemplo

**Entrada:** foto de un frasco ámbar con la etiqueta

```
Sigma-Aldrich
Sodium Chloride, ACS reagent, ≥99.0%
S9888-500G          Lot# SLCK3421
500 g
CAS 7647-14-5
Store at RT
Exp: 03/2028
```

**Salida:**

```json
{
  "producto": "Sodium Chloride, ACS reagent, ≥99.0%",
  "fabricante": "Sigma-Aldrich",
  "numero_catalogo": "S9888-500G",
  "lote": "SLCK3421",
  "cantidad": { "valor": 500, "unidad": "g" },
  "concentracion": null,
  "fecha_vencimiento": "2028-03-31",
  "temperatura_almacenamiento": "temperatura ambiente",
  "pictogramas_ghs": [],
  "cas": "7647-14-5",
  "confianza": "alta",
  "campos_ilegibles": []
}
```

## Reglas duras

1. **Nunca inventes un valor.** Si un campo no está en la etiqueta o no se puede leer, poné `null` y agregá el nombre del campo a `campos_ilegibles`. Un `null` explícito es un dato correcto; un valor inventado es un error que se propaga a todo el inventario.

2. **Fechas.** Convertí siempre a `YYYY-MM-DD`. Si la etiqueta solo tiene mes y año (`03/2028`), usá el **último día de ese mes** (`2028-03-31`), porque así es como se interpreta un vencimiento. Si el formato es ambiguo entre día/mes y mes/día, poné `null` y anotá `fecha_vencimiento` en `campos_ilegibles`.

3. **Unidades.** Transcribí la unidad tal como aparece (`g`, `mg`, `mL`, `L`, `U/mL`, `mM`). **No conviertas** entre unidades.

4. **Concentración vs. cantidad.** `cantidad` es cuánto hay en el envase (500 g). `concentracion` es cuán fuerte es (1 M, 10 mg/mL). Un sólido puro suele tener cantidad y no concentración.

5. **Pictogramas GHS.** Listá solo los que ves. Nombres válidos: `explosivo`, `inflamable`, `comburente`, `gas_a_presion`, `corrosivo`, `toxico_agudo`, `irritante`, `peligro_salud`, `peligro_ambiental`.

6. **Confianza.**
   - `alta`: la etiqueta está enfocada, completa y legible.
   - `media`: hay reflejos, ángulo o desenfoque parcial, pero los campos principales se leen.
   - `baja`: la mitad o más de la etiqueta no se lee. Si es `baja`, **decilo**: no devuelvas un JSON optimista.

7. **Idioma.** El contenido de la etiqueta se transcribe tal cual (si dice "Sodium Chloride", no lo traduzcas). Los valores de enumeración (`temperatura_almacenamiento`, pictogramas, `confianza`) van en español.

## Casos borde

- **Múltiples etiquetas en una foto:** devolvé un array JSON de objetos.
- **La foto no es una etiqueta de laboratorio:** devolvé `{"error": "no_es_etiqueta_de_laboratorio"}`.
- **La etiqueta está en un idioma que no reconocés:** transcribí igual lo que ves y bajá la `confianza`.
- **Hay un código de barras o QR:** ignoralo. No intentes decodificarlo desde la imagen.
