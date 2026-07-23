# Gemma 4 multimodal en tu laptop — Ollama

Tres modalidades (texto, imagen, audio) sobre **el mismo modelo**, corriendo
100% local. Sin pipeline de ASR separado, sin encoder de visión separado, sin
internet: Gemma 4 12B es *encoder-free* — imagen y audio entran directo al
backbone del LLM.

Usalo como base para cualquier proyecto que procese texto clínico, imágenes
médicas o dictado por voz **sin que el dato salga de la máquina**.

## Setup

```bash
ollama pull gemma4:12b     # ~8 GB; verificá el tag exacto con `ollama list`
pip install ollama
```

En `assets/` ya hay material de ejemplo:

- `radiografia.jpg` — radiografía de tórax PA normal ([Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Normal_posteroanterior_(PA)_chest_radiograph_(X-ray).jpg), licencia libre)
- `dictado.wav` — dictado clínico **sintético** (TTS), 19 s. Sin datos de pacientes reales.

Reemplazalos por tu propio material cuando armes tu proyecto — y anonimizá antes.

## Correr

```bash
python demo_multimodal.py texto      # baseline de latencia
python demo_multimodal.py imagen     # visión sin encoder → JSON estructurado
python demo_multimodal.py audio      # audio nativo (ver ⚠️ abajo)
```

Si el 12B se arrastra en tu máquina, bajá a `gemma4:e4b` (editá `MODELO` en el
script). Un modelo que responde más lento sigue siendo un modelo que funciona.

## ⚠️ Audio: la capacidad es del modelo, el soporte es del runtime

**Verificado (jul-2026, Ollama 0.31.2): Ollama todavía no soporta entrada de
audio.** El campo `audios` se descarta *en silencio* — sin error — y el modelo
responde como si no hubiera audio adjunto. Es el ejemplo perfecto de una lección
que te va a servir toda la carrera:

> Cuando algo no anda, chequeá el runtime antes de culpar al modelo.

El modelo SÍ tiene audio nativo. Para usarlo hoy, el camino verificado es
**LiteRT-LM CLI** (el mismo runtime del AI Edge Gallery):

```bash
uv tool install --python 3.12 litert-lm    # con Python 3.14 aún no hay wheel

litert-lm run \
  --from-huggingface-repo=litert-community/gemma-4-E2B-it-litert-lm \
  gemma-4-E2B-it.litertlm \
  --prompt="Escuchá este dictado clínico y devolvé JSON con: transcripcion_literal, motivo_consulta, hallazgos (array), plan (array), terminos_dudosos (array). No inventes nada que no se haya dicho." \
  --attachment assets/dictado.wav
```

`--attachment` también acepta imágenes — te sirve como segundo camino de visión.

### Un detalle que vale la pena estudiar

En nuestras pruebas, el modelo transcribió *"hipoventilación en base pulmonar
derecha"* como *"pavimentación en pulmonar derecha"* en una corrida y como
*"movilización en pulmonar derecha"* en otra — **y en ninguna lo marcó en
`terminos_dudosos`**. El término técnico que no entiende lo reemplaza por una
palabra plausible *distinta cada vez*, con total confianza: no es un error
fijo, es incertidumbre no reportada. Si tu proyecto usa audio clínico, ese es
exactamente el tipo de fallo que tu evaluación tiene que detectar. El modelo
que dice "no entendí esta palabra" vale más que el que inventa una parecida.
