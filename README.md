# Gemma 4 × UNER — IA para la Salud

### Material de los encuentros preparatorios del hackathon · ejemplos base para tu proyecto

**📽 Slides de los encuentros:** https://matiasmolinas.github.io/gemma4-uner/
**📬 Consultas:** ciev.ingenieria@uner.edu.ar

Este repo contiene todo lo que se muestra en los dos encuentros (16 y 23 de julio,
virtuales), listo para que lo clones y lo uses como **punto de partida de tu
proyecto**: demos de Gemma 4 corriendo local, una skill multimodal para el
celular, notebooks de fine-tuning y multi-LoRA en Colab gratis.

---

## Qué hay acá

```
gemma4-uner/
├── docs/                             ← las slides (markdown + visor web)
│
├── notebooks/                        ← corren en Colab GRATIS (T4)
│   ├── 01_gemma4_escalera.ipynb      ← Gemma 4 en Colab: texto, thinking, multimodal
│   ├── 02_finetune_qlora.ipynb       ← fine-tuning QLoRA con Unsloth, con baseline
│   └── 03_multilora_vllm.ipynb       ← un base + N adapters con vLLM
│
├── skills/
│   └── lab-label-extractor/          ← skill multimodal: foto de etiqueta → JSON
│       ├── SKILL.md                  ← para importar en Google AI Edge Gallery
│       ├── scripts/index.html        ← la vista que renderiza el JSON
│       └── web/                      ← la misma skill corriendo en el BROWSER (WebGPU)
│
└── demos/
    ├── ollama/                       ← texto / imagen / audio en tu laptop
    └── agente/                       ← function calling nativo, agente multi-paso
```

---

## Empezar en 5 minutos

```bash
git clone https://github.com/matiasmolinas/gemma4-uner.git
cd gemma4-uner

# 1. Gemma 4 local
ollama pull gemma4:e4b        # liviano (edge / agentes)
ollama pull gemma4:12b        # multimodal encoder-free (necesita ~16 GB)

# 2. Demo multimodal en tu laptop
cd demos/ollama
pip install ollama
python demo_multimodal.py texto
python demo_multimodal.py imagen     # usa assets/radiografia.jpg

# 3. Agente con function calling
cd ../agente
python agente_gemma4.py
```

Para el celular: instalá **Google AI Edge Gallery** (Android/iOS), descargá
Gemma 4 E4B *adentro de la app*, e importá `skills/lab-label-extractor/SKILL.md`.
Después ponelo en modo avión y comprobá que sigue funcionando: **el dato nunca
salió de tu bolsillo.** Esa es la tesis de todo esto.

---

## Estado: qué está probado y qué no

Probado el 23-jul-2026 en una MacBook M4 de 16 GB (Ollama 0.31.2):

| Componente | Estado | Nota |
|---|---|---|
| `demos/ollama` texto e imagen (`gemma4:12b`) | ✅ | |
| `demos/ollama` audio | ⚠️ | **Ollama todavía no soporta audio** (descarta el campo en silencio). Funciona vía LiteRT-LM CLI — ver `demos/ollama/README.md` |
| `demos/agente` (`gemma4:e4b`) | ✅ | Cadena de 4 pasos autónoma; sabe cuándo NO llamar tools |
| Skill web en browser (WebGPU) | ✅ texto | La variante web de Gemma 4 es **text-only por ahora** (model card oficial); visión: Gallery o LiteRT-LM |
| Notebooks de Colab | ⚠️ | Verificá el estado en cada notebook antes de confiar |

Los dos ⚠️ son la lección más importante del material:
**la capacidad es del modelo, el soporte es del runtime. Cuando algo no anda,
chequeá el runtime antes de culpar al modelo.** Te va a pasar en el hackathon.

---

## Los IDs de modelo cambian

Los nombres de modelos y tags cambian entre releases. Antes de debuggear
cualquier otra cosa, verificá el identificador:

| Dónde | Cómo verificar |
|---|---|
| Ollama | `ollama list` después de `ollama pull gemma4` |
| Hugging Face | https://huggingface.co/google (`gemma-4-E4B-it`, `gemma-4-12B-it`) |
| LiteRT (celular/browser) | https://huggingface.co/litert-community |
| Unsloth (fine-tuning) | https://unsloth.ai/docs/models/gemma-4/train |
| MedGemma | https://huggingface.co/google/medgemma-1.5-4b-it |

---

## Cómo se juzga tu proyecto (no es secreto)

- **30% — ¿Midieron algo?** Baseline primero, número después. Sin evaluación no hay proyecto, hay demo.
- **25% — ¿El dato está protegido?** PHI a una API de terceros = muerto por diseño.
- **25% — ¿Corre?** En vivo, en su máquina. No un video, no un slide.
- **20% — ¿Saben dónde falla?** Si dicen que funciona siempre, no lo probaron.

**No puntúa:** el tamaño del modelo, la cantidad de features, lo lindo del frontend.

### Los siete errores más comunes (evitálos y estás en el 10% de arriba)

1. **Data leakage a nivel de paciente** — cortes del mismo paciente en train y test. El error #1.
2. **Sin baseline** — un número solo no es un resultado.
3. **PHI en una API de terceros** — muerte instantánea.
4. **Métrica equivocada** — accuracy sobre datos desbalanceados no dice nada; usá F1, AUC o sensibilidad/especificidad.
5. **Demo grabada** — si no corre en vivo, no corre.
6. **Chat template mismatch** — funciona en el notebook, se rompe en la app.
7. **«El modelo dijo X» = «X es verdad»** — no. El modelo dijo X. Eso es todo lo que sabés.

A la sesión de feedback traé tres cosas: **tu baseline, tu métrica, y el caso
donde tu proyecto falla.** Con eso se puede dar feedback útil en 3 minutos.

---

## Armar el equipo: cinco roles

No hacen falta cinco personas; hace falta que alguien se haga cargo de cada rol:
**Datos** (el 80% del trabajo) · **Modelo** · **Evaluación** · **Dominio/clínica** ·
**Writeup y demo**. El equipo con alguien de salud adentro tiene una ventaja injusta.

---

## Fuentes

| Tema | Fuente |
|---|---|
| Familia Gemma 4, arquitectura | `ai.google.dev/gemma/docs/core` |
| 12B encoder-free | Blog de Google, "Introducing Gemma 4 12B" |
| PLE, MoE, memoria | Model card de `google/gemma-4-31B-it` en HF |
| Agent Skills on-device | Google Developers Blog, "Bring state-of-the-art agentic skills to the edge with Gemma 4" |
| Gemma 4 web (text-only hoy) | Model card de `litert-community/gemma-4-E2B-it-litert-lm` |
| VRAM de fine-tuning | Documentación de Unsloth |
| MedGemma 1.5 | Technical Report, arXiv 2604.05081 |
| Multi-LoRA | Documentación de vLLM |
| LoRA Land | arXiv 2405.00732 |
| MRI 33% → 89% | Tutorial de fine-tuning de MedGemma, DataCamp |

---

## Licencias — leé esto antes de publicar tu proyecto

- **Este repo: Apache 2.0** (ver `LICENSE`). Usalo como quieras.
- **Gemma 4: Apache 2.0.** Comercialmente permisiva.
- **MedGemma: Health AI Developer Foundations terms of use — NO es Apache.**
  Leéla antes de armar una empresa arriba.
- MedGemma 1.5 sigue siendo base Gemma 3, no Gemma 4. **Fine-tunear Gemma 4 al
  dominio médico es un hueco abierto** — una oportunidad (o una tesis).
- La radiografía de ejemplo proviene de
  [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Normal_posteroanterior_(PA)_chest_radiograph_(X-ray).jpg)
  (licencia libre). El dictado de ejemplo es TTS sintético — **sin datos de
  pacientes reales**. Hacé lo mismo en tu proyecto: anonimizá antes de tocar nada.

---

## Y lo más importante

Nada de esto es un dispositivo médico. Ni MedGemma, ni Gemma 4, ni lo que
construyas este fin de semana. El EU AI Act clasifica la IA médica como alto
riesgo, y la responsabilidad es del que despliega, no del que entrena.

**El modelo es lo fácil. Los datos, la evaluación y la regulación son el trabajo.**

Ahora andá y construí algo.
