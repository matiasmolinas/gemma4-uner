# lab-label-extractor — versión web (plan B del Gallery)

La misma skill del práctico, pero corriendo **Gemma 4 en el browser** vía WebGPU
con MediaPipe LLM Inference. Todo client-side: el modelo se carga desde un
archivo local y **la foto no sale de la máquina**. Ideal para el Encuentro 2
(virtual): compartís la pestaña de Chrome y no dependés del teléfono ni de scrcpy.

## Setup (una sola vez, antes de la charla)

1. **Descargá el modelo web** desde [litert-community en Hugging Face](https://huggingface.co/litert-community)
   (repos sin gate, no hace falta login):
   - [`gemma-4-E2B-it-web.litertlm`](https://huggingface.co/litert-community/gemma-4-E2B-it-litert-lm) — el seguro para 16 GB de RAM.
   - [`gemma-4-E4B-it-web.litertlm`](https://huggingface.co/litert-community/gemma-4-E4B-it-litert-lm) — mejor extracción si la máquina da.

   ⚠️ Tiene que ser la variante **`-web`** (formato `.litertlm` convertido para
   browser). El checkpoint de Ollama **no sirve** acá — mismo principio que en
   el Gallery.

2. **Abrí `index.html` en Chrome** (doble clic alcanza). Necesita WebGPU:
   Chrome o Edge actualizado; en una Mac M-series anda directo.

## Uso

1. **Modelo** → "Elegir archivo .litertlm" y seleccioná el que descargaste.
   La primera carga a GPU tarda 1–3 minutos; después de eso queda en memoria
   mientras no cierres la pestaña. **Cargalo antes de empezar la charla.**
2. **Etiqueta** → arrastrá una foto, o clic para elegirla (en un teléfono abre
   la cámara). La imagen se reduce a 768 px del lado mayor para acelerar el prefill.
3. **Digitalizar** → streaming del JSON en vivo + la tarjeta renderizada
   (mismo renderer que `scripts/index.html`) + tiempos de primer token y total.

El botón **"Modo ensayo (sin modelo)"** renderiza el dato de ejemplo sin cargar
nada: sirve para practicar el guion y como red de contención si el modelo no
carga en vivo.

## Qué decir en la demo

- "Es el mismo `SKILL.md` del Gallery, inyectado como prompt. **La skill es el
  contrato, no la plataforma**: teléfono, browser, mismo archivo."
- Abrí las DevTools → pestaña Network mientras corre la inferencia: **cero
  requests**. Es el equivalente browser del modo avión del teléfono.
- Los tiempos en pantalla (primer token / total) son el reemplazo del argumento
  de latencia del proyector.

## ⚠️ Verificado 23-jul-2026: la variante web de Gemma 4 es TEXT-ONLY

El model card oficial lo dice: *"Web on LiteRT-LM uses a specially optimized
model for Web… Currently the model is text-only."* La visión en browser falla con
`LlmVisionInferenceCalculator: Image models could not be created`.

**Lo que funciona hoy (probado en esta máquina, M4):**
- Modo **texto** end-to-end: modelo listo en ~5 s, primer token 1.3 s, JSON
  completo en ~5 s. La página tiene un campo para pegar el texto de la etiqueta.
- El modelo (`gemma-4-E2B-it-web.litertlm`, 1.9 GB) y una etiqueta de prueba
  (`etiqueta_prueba.jpg`) ya están en esta carpeta.

**Para el flujo con FOTO (Gemma 4 con visión, on-device):** LiteRT-LM CLI, verificado:

```bash
litert-lm run \
  ~/.litert-lm/cache/huggingface/litert-community/gemma-4-E2B-it-litert-lm/gemma-4-E2B-it.litertlm \
  --prompt="<el prompt de la skill>" \
  --attachment etiqueta_prueba.jpg
```

Extrajo la etiqueta de prueba correctamente, incluida la regla de fechas
(11/2027 → 2027-11-30). Falló en un pictograma (no vio `irritante`) — usalo
como contenido.

## Puntos frágiles

- El **CDN de jsdelivr** se necesita una vez al abrir la página (la librería JS).
  Abrí la página antes de la charla para que quede en caché del browser.
- La API de MediaPipe para web está en **modo mantenimiento** (Google recomienda
  migrar a LiteRT-LM JS). Para esta demo alcanza, pero verificá que siga andando
  la semana de la charla, como todo lo demás del repo.
- Si el JSON sale malformado, la página muestra la salida cruda del modelo en
  vez de romperse — eso también es contenido: "los modelos chicos imitan mejor
  de lo que obedecen".
