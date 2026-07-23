# Demo de laptop — Ollama

Peldaño 2 de la escalera (Charla 1, slide 8).

## Setup

```bash
ollama pull gemma4:12b     # verificá el tag con `ollama list`
pip install ollama
```

Poné en `assets/`:
- `radiografia.jpg` — una imagen médica real (o una etiqueta de laboratorio)
- `dictado.wav` — 15–20 s de dictado clínico grabado por vos

## Correr

```bash
python demo_multimodal.py texto     # baseline, calibra latencia con el proyector
python demo_multimodal.py imagen    # visión sin encoder
python demo_multimodal.py audio     # audio nativo, sin ASR separado
```

## ⚠️ El punto frágil

**El soporte de audio vía Ollama depende de la versión del runtime.** Es la parte
más probable de romperse en vivo.

**VERIFICADO 23-jul-2026 (Ollama 0.31.2): audio NO funciona.** El campo `audios`
se descarta en silencio (cliente Python y API REST); el modelo responde "quedo a
la espera del material". Pasar el wav por `images` cuelga la request. Mostrar el
fallo en vivo ES la lección: "chequeá el runtime antes de culpar al modelo".

Fallback **verificado y funcionando** — LiteRT-LM CLI (instalar con Python 3.12;
con 3.14 no hay wheel):

```bash
uv tool install --python 3.12 litert-lm
litert-lm run \
  ~/.litert-lm/cache/huggingface/litert-community/gemma-4-E2B-it-litert-lm/gemma-4-E2B-it.litertlm \
  --prompt="Escuchá este dictado clínico y devolvé JSON con: transcripcion_literal, motivo_consulta, hallazgos (array), plan (array), terminos_dudosos (array). No inventes nada que no se haya dicho." \
  --attachment assets/dictado.wav
```

(El modelo ya está descargado en ese path. `--attachment` también acepta imágenes.)

Bonus pedagógico verificado: transcribió "hipoventilación en base pulmonar derecha"
como "pavimentación en pulmonar derecha" y NO lo marcó en `terminos_dudosos` —
ejemplo perfecto, en vivo, de por qué la regla "null explícito > valor inventado"
importa.

Y si eso también falla: **el video de backup**. Grabalo.

## Guion de la demo

1. `texto` — "esto es el baseline; miren la latencia con el proyector conectado".
2. `imagen` — arrastrás la imagen. JSON estructurado. "Sin encoder de visión."
3. `audio` — pasás el `.wav`. "Un solo modelo. Sin pipeline de ASR. El audio del
   paciente no salió de esta máquina."

Si el 12B se arrastra con el proyector conectado, **bajá a `e4b` y decilo en voz alta**:
*"miren, con el proyector el 12B se arrastra — esto también es información útil."*
Convertís un problema en contenido.
