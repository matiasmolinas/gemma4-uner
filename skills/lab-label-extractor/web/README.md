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
- **LiteRT-LM CLI** en la compu:

```bash
uv tool install --python 3.12 litert-lm
litert-lm run \
  --from-huggingface-repo=litert-community/gemma-4-E2B-it-litert-lm \
  gemma-4-E2B-it.litertlm \
  --prompt="<el prompt de la skill>" \
  --attachment etiqueta_prueba.jpg
```

En nuestra prueba extrajo la etiqueta correctamente, incluida la regla de
fechas (11/2027 → `2027-11-30`)… y falló en un pictograma (vio `inflamable`
pero no `irritante`). Ese tipo de fallo parcial es exactamente lo que tu
evaluación tiene que medir.

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
