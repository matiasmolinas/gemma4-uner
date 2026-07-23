# lab-label-extractor — versión web

La misma skill, pero corriendo **Gemma 4 en el browser** vía WebGPU con
MediaPipe LLM Inference. Todo es client-side: el modelo se carga desde un
archivo local y **el dato nunca sale de tu máquina** (abrí DevTools → Network
mientras corre: cero requests).

Usala como base si tu proyecto necesita un frontend web con el modelo
on-device — sin backend, sin API keys, sin costos de inferencia.

## Setup (una sola vez)

1. **Descargá el modelo web** desde [litert-community en Hugging Face](https://huggingface.co/litert-community)
   (repos sin gate, no hace falta login):
   - [`gemma-4-E2B-it-web.litertlm`](https://huggingface.co/litert-community/gemma-4-E2B-it-litert-lm) (~1.9 GB) — el seguro para 16 GB de RAM.
   - [`gemma-4-E4B-it-web.litertlm`](https://huggingface.co/litert-community/gemma-4-E4B-it-litert-lm) — mejor extracción si la máquina da.

   ⚠️ Tiene que ser la variante **`-web`** (`.litertlm` convertido para browser).
   El checkpoint de Ollama **no sirve** acá — cada runtime tiene su formato.

2. **Abrí `index.html` en Chrome** (doble clic alcanza). Necesita WebGPU:
   Chrome o Edge actualizado.

## Uso

1. **Modelo** → "Elegir archivo .litertlm". La primera carga a GPU tarda un
   rato; después queda en memoria mientras no cierres la pestaña.
2. **Etiqueta** → pegá el texto de la etiqueta (ver ⚠️ abajo), o cargá una foto.
3. **Digitalizar** → streaming del JSON en vivo + la tarjeta renderizada +
   tiempos de primer token y total.

El botón **"Modo ensayo (sin modelo)"** muestra el resultado de ejemplo sin
cargar nada — útil para ver la UI antes de bajar el modelo.

## ⚠️ Estado actual: la variante web de Gemma 4 es TEXT-ONLY

Del model card oficial: *"Web on LiteRT-LM uses a specially optimized model for
Web… Currently the model is text-only."* Si intentás visión, falla con
`LlmVisionInferenceCalculator: Image models could not be created` (la página lo
detecta y te lo explica).

**Rendimiento verificado (jul-2026, MacBook M4, E2B web):** modelo listo en ~5 s,
primer token 1.3 s, JSON completo en ~5 s.

**Para el flujo con FOTO** (Gemma 4 con visión, on-device) tenés dos caminos:

- **AI Edge Gallery** en el celular (el camino principal de la skill), o
- **LiteRT-LM CLI** en la compu — comando verificado (~10 s con el modelo cacheado):

```bash
uv tool install --python 3.12 litert-lm   # una sola vez

litert-lm run \
  --from-huggingface-repo=litert-community/gemma-4-E2B-it-litert-lm \
  gemma-4-E2B-it.litertlm \
  --prompt="Extraé los datos de esta etiqueta de laboratorio y devolvé únicamente JSON con: producto, fabricante, numero_catalogo, lote, cantidad, fecha_vencimiento (YYYY-MM-DD), pictogramas_ghs, cas, confianza, campos_ilegibles" \
  --attachment etiqueta_prueba.jpg
```

En nuestras pruebas extrajo la etiqueta correctamente, con un matiz que importa:
con este prompt corto la fecha "11/2027" sale `2027-11-01`; con el contenido
completo de la SKILL.md como prompt sale `2027-11-30` (la regla del último día
del mes). El detalle completo está en el [README de la skill](../README.md) —
las reglas de la skill son el contrato, no decoración.

## Notas técnicas

- La página usa el patrón oficial de MediaPipe: import ES desde el CDN de
  jsdelivr + `modelAssetBuffer` con stream reader (necesario para modelos de GB).
- La API de MediaPipe para web está en **modo mantenimiento**; Google recomienda
  migrar a LiteRT-LM JS. Para un prototipo de hackathon alcanza.
- `etiqueta_prueba.jpg` es una etiqueta sintética generada para probar: fecha
  ambigua, pictogramas GHS, unidades. Reemplazala por fotos reales de tu lab.
- Si el modelo devuelve el JSON envuelto en fences o con texto alrededor, la
  página lo limpia; si sale malformado, muestra la salida cruda. Los modelos
  chicos **imitan mejor de lo que obedecen** — dale ejemplos, no especificaciones.
