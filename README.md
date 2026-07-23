# Gemma 4 — UNER Bioingeniería

### Material completo de los dos encuentros preparatorios · previo al hackathon "Build with Gemma · IA para la Salud"

**📽 Presentación:** https://matiasmolinas.github.io/gemma4-uner/ (29 slides, `N` muestra las notas del orador)

---

## Qué hay acá

```
gemma4-uner/
├── docs/
│   ├── presentacion.md               ← el deck completo en markdown (con notas del orador)
│   └── index.html                    ← visor de slides (GitHub Pages)
├── GUION.md                          ← el guion slide por slide, con fuentes
├── AJUSTE-agenda-oficial.md          ← cómo se reorganizó el material según el flyer oficial
│
├── notebooks/
│   ├── 01_gemma4_escalera.ipynb      ← Encuentro 1. Colab gratis.
│   ├── 02_finetune_qlora.ipynb       ← Encuentro 2. QLoRA en T4.
│   └── 03_multilora_vllm.ipynb       ← Encuentro 2. EL CLÍMAX.
│
├── skills/
│   └── lab-label-extractor/
│       ├── SKILL.md                  ← la skill que se escribe EN VIVO
│       ├── scripts/index.html        ← la vista que renderiza el JSON
│       └── web/                      ← la skill corriendo en el BROWSER (WebGPU)
│
└── demos/
    ├── ollama/
    │   ├── demo_multimodal.py        ← texto / imagen / audio en la laptop
    │   └── assets/                   ← radiografia.jpg + dictado.wav
    └── agente/
        └── agente_gemma4.py          ← function calling nativo, multi-paso
```

---

## ✅ Estado de verificación (23-jul-2026, MacBook M4 16 GB, Ollama 0.31.2)

| Demo | Estado | Nota |
|---|---|---|
| Ollama texto (`gemma4:12b`) | ✅ | ~70 s con carga de modelo incluida |
| Ollama imagen | ✅ | JSON estructurado correcto sobre la radiografía |
| Ollama audio | ❌ → ✅ | **Ollama 0.31.2 descarta `audios` en silencio.** El fallback LiteRT-LM CLI funciona (ver `demos/ollama/README.md`) |
| Agente function calling (`gemma4:e4b`) | ✅ | Cadena de 4 pasos autónoma + sabe NO llamar tools |
| Skill en browser (WebGPU, E2B web) | ✅ texto | La variante web de Gemma 4 es **text-only por ahora** (model card oficial). Visión con foto: Gallery o LiteRT-LM CLI |

Los hallazgos de audio y de visión web **son contenido de la charla**, no vergüenzas:
*"cuando algo no anda, chequeá el runtime antes de culpar al modelo."*

---

## ⚠️ LEER ANTES DE PRESENTAR

**Los IDs de modelo cambian entre releases.** Todo lo que está acá sale de
documentación oficial, pero **verificá cada identificador** antes de la charla:

| Dónde | Qué verificar | Cómo |
|---|---|---|
| Ollama | el tag exacto | `ollama list` después de `ollama pull gemma4` |
| Hugging Face | `google/gemma-4-E4B-it`, `google/gemma-4-12B-it` | https://huggingface.co/google |
| LiteRT | `litert-community/gemma-4-*-litert-lm` | https://huggingface.co/litert-community |
| Unsloth | `unsloth/gemma-4-E4B-it` y los números de VRAM | https://unsloth.ai/docs/models/gemma-4/train |
| MedGemma | `google/medgemma-1.5-4b-it` | https://huggingface.co/google/medgemma-1.5-4b-it |
| Gallery | formato de import de skills | https://github.com/google-ai-edge/gallery |

**Los notebooks no fueron ejecutados contra hardware real.** Corré los tres,
completos, **al menos 48 h antes**. Los demos de `demos/` y la skill web sí
fueron verificados (tabla de arriba).

---

## Checklist previo (48 h antes)

- [x] `ollama pull gemma4:12b` y `ollama pull gemma4:e4b`
- [x] `assets/radiografia.jpg` y `assets/dictado.wav` en su lugar
- [x] Demos de Ollama y agente corridos de punta a punta
- [x] Fallback de audio (LiteRT-LM CLI) instalado y probado
- [x] Skill web probada en Chrome con el modelo descargado
- [ ] AI Edge Gallery instalado, con E4B **descargado adentro de la app**
- [ ] Skill `lab-label-extractor` importada y probada en el Gallery
- [ ] Los 3 notebooks ejecutados una vez de punta a punta
- [ ] El prompt-trampa del anti-hype probado: **tiene que fallar de forma convincente**
- [ ] Espejado del celular a Meet probado (scrcpy / AirPlay)
- [ ] Videos de backup de las demos (30–60 s c/u)
- [ ] Ensayo de escribir la SKILL.md en vivo, **tres veces**
- [ ] **Asumir que no hay wifi.** Todo tiene que andar offline (salvo el propio Meet).

---

## Los tres momentos que definen las charlas

**1. El teléfono en modo avión** (Encuentro 1).
Único truco escénico. Poné el avión, seguí prompteando. Es el instante en que
entienden que la computadora que ya tienen alcanza.

**2. Escribir la SKILL.md en vivo** (Encuentro 2).
Si escribís una skill funcional en 13 minutos frente a ellos, ganaste el hackathon
antes de que empiece. Ensayalo tres veces.

**3. El diagrama de multi-LoRA** (Encuentro 2).
Un base, cuatro especialistas, sesenta megas cada uno. *"Esto es lo que estoy
construyendo, y ustedes lo pueden construir este fin de semana."*

---

## Fuentes principales

| Tema | Fuente |
|---|---|
| Familia Gemma 4, arquitectura | `ai.google.dev/gemma/docs/core` |
| 12B encoder-free | Blog de Google, "Introducing Gemma 4 12B" |
| PLE, MoE, memoria | Model card de `google/gemma-4-31B-it` en HF |
| Agent Skills on-device | Google Developers Blog, "Bring state-of-the-art agentic skills to the edge with Gemma 4" |
| Gemma 4 web (text-only hoy) | Model card de `litert-community/gemma-4-E2B-it-litert-lm` |
| VRAM de fine-tuning | Documentación de Unsloth (autoritativa) |
| MedGemma 1.5 | Technical Report, arXiv 2604.05081 |
| MedASR | Google Research Blog |
| Multi-LoRA | Documentación de vLLM |
| LoRA Land (el dato defendible) | arXiv 2405.00732 |
| MRI 33% → 89% | Tutorial de fine-tuning de MedGemma, DataCamp |

Todas las citas específicas, con la frase exacta que respalda cada número, están
en `GUION.md`.

---

## Licencias — decilo en voz alta

- **Este repo: Apache 2.0** (ver `LICENSE`).
- **Gemma 4: Apache 2.0.** Comercialmente permisiva.
- **MedGemma: Health AI Developer Foundations terms of use. NO es Apache.**
  Léela antes de armar una empresa arriba.
- **MedGemma 1.5 sigue siendo Gemma 3**, no Gemma 4.
- **Nadie fine-tuneó Gemma 4 al dominio médico todavía.** Eso no es un ejercicio
  de hackathon. Es una tesis.
- La radiografía de ejemplo (`demos/ollama/assets/radiografia.jpg`) proviene de
  [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Normal_posteroanterior_(PA)_chest_radiograph_(X-ray).jpg)
  (licencia libre). El dictado es TTS sintético — sin datos de pacientes reales.

---

## Y lo más importante

Nada de esto es un dispositivo médico. Ni MedGemma, ni Gemma 4, ni lo que
construyan este fin de semana. La responsabilidad es del que despliega, no del
que entrena.

**El modelo es lo fácil. Los datos, la evaluación y la regulación son el trabajo.**
