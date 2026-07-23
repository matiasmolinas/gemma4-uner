# AJUSTE — Reestructuración según la agenda oficial del flyer

El flyer de los **Encuentros Virtuales Preparatorios** trae dos cosas que cambian el material:

1. **La agenda ya fue anunciada**, y no coincide con la que yo había armado. Los estudiantes se anotaron esperando *esos* temas, así que el deck se reorganizó para respetarlos al pie de la letra.
2. **Son 100% virtuales por Google Meet, 18:00 h.** No hay proyector: todo es pantalla compartida. Eso cambia el riesgo principal (tu conexión, no el cable) y el modo de hacer las demos.

El deck nuevo (29 slides, paleta azul del flyer) vive ahora en **`docs/presentacion.md`**, publicado como slides en GitHub Pages (`docs/index.html`); los `.pptx` originales fueron retirados del repo. El guion original (`GUION.md`) sigue siendo válido para el *contenido y las fuentes* de cada bloque; lo que cambió es **dónde vive cada bloque** y el agregado de tres slides nuevas.

---

## Mapa: agenda anunciada → slides

### ENCUENTRO 1 — "Inmersión" (16 jul)
Agenda del flyer: *¿Qué es Build with Gemma? · Conocé Gemma 4 · Reglas del hackathon · Ideas y formación de equipos*

| Bloque anunciado | Slides | Notas |
|---|---|---|
| **¿Qué es Build with Gemma?** | Portada, divider, agenda, quién habla, "¿Qué es Build with Gemma?", la tesis | La iniciativa de Google + el tema "IA para la salud" + por qué open weights |
| **Conocé Gemma 4** | Familia (nivel inmersión), 12B encoder-free, la escalera, anti-hype | **Sin** PLE/MoE en detalle — eso se movió al Encuentro 2 |
| **Ideas y formación de equipos** | El menú (MedGemma), **formación de equipos (slide nueva)** | El menú = "ideas"; los 5 roles = "formación de equipos" |
| **Reglas del hackathon** | Cómo los voy a juzgar + guardrail regulatorio, cierre + tarea | Criterios de jurado + "no es dispositivo médico" como regla |

### ENCUENTRO 2 — "Hands-on técnico" (23 jul)
Agenda del flyer: *Taller práctico con Gemma 4 (Ollama + Unsloth) · Function calling y multimodalidad · Feedback de proyectos · Preparación de la entrega: Writeup, demo y Kaggle*

| Bloque anunciado | Slides | Notas |
|---|---|---|
| **Taller (Ollama + Unsloth)** | Divider, agenda, PLE/MoE (ahora acá), LoRA 90s, VRAM, 4 trampas, FT vs RAG + 33→89 | Ollama al principio, Unsloth en el medio |
| **Function calling y multimodalidad** | Los dos ejes, function calling + skill en vivo, gotcha runtime + tamaño para agentes | La demo de SKILL.md vive acá |
| **Feedback de proyectos** | Honestidad epistémica, multi-LoRA, **los 7 errores (slide nueva)** | El anexo B del guion convertido en slide |
| **Preparación de la entrega** | **Writeup / demo / Kaggle (slide nueva)**, cierre | Licencia (Apache vs HAI-DEF) va acá, que es cuando importa |

---

## Las tres slides nuevas

1. **Formación de equipos (E1).** Cinco roles: Datos, Modelo, Evaluación, Dominio/clínica, Writeup. El mensaje: no hacen falta cinco personas, hace falta que alguien se haga cargo de cada rol. El equipo con un clínico adentro tiene ventaja injusta.

2. **Los 7 errores que voy a marcar (E2).** Es el Anexo B del guion, ahora visible. Cierra pidiéndoles que traigan a la sesión de feedback tres cosas: su baseline, su métrica, y el caso donde su proyecto falla. Con eso das feedback útil en tres minutos.

3. **Writeup / demo / Kaggle (E2).** Qué contiene un buen writeup, cómo se ve una buena demo (corre en vivo, muestra el fallo), y cómo se entrega en Kaggle. La nota de licencia y el MedGemma Impact Challenge (US$100K) cierran acá.

---

## Ajustes por ser remoto (Google Meet)

- **El riesgo principal ahora es tu conexión.** Si tu internet se cae, se cae la reunión. Ten los clips de backup de cada demo **listos para reproducir**, no solo grabados.
- **La escalera (E1) y todas las demos** son pantalla compartida. Eso es más fácil que con proyector, no más difícil.
- **El modo avión del celular:** espejá la pantalla del teléfono hacia la ventana de Meet (scrcpy en Android, AirPlay/QuickTime en iOS). El truco sigue funcionando y sigue siendo la mejor prueba visual de "el dato no salió del dispositivo".
- **Escribir la SKILL.md en vivo (E2):** compartís el editor por pantalla. Menos presión que en vivo físico, pero **ensayalo igual tres veces** — el chat de Meet se llena de "no se ve" si te trabás.
- **Feedback de proyectos:** en remoto conviene formato office-hours con turnos. Pediles de antemano el baseline + métrica + caso de fallo por escrito, así aprovechás los minutos.

---

## Lo que NO cambió

- Todas las **fuentes y citas** del `GUION.md` siguen valiendo; solo se reubicó el contenido.
- Los **notebooks, la skill y los demos** del repo no cambian: `01_gemma4_escalera` sirve al Encuentro 1; `02_finetune_qlora` y `03_multilora_vllm` sirven al Encuentro 2; la skill `lab-label-extractor` es la demo del bloque de function calling.
- El **checklist previo** sigue igual, más un ítem nuevo: **crear cuenta de Kaggle** (la entrega es ahí, dato del flyer).

---

## Advertencia que se mantiene

Los IDs de modelo cambian entre releases y ninguno de los notebooks fue ejecutado contra hardware real. Verificá cada identificador y corré los tres notebooks de punta a punta **antes** de cada encuentro. Todo lo del README maestro sigue aplicando.
