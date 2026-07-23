# IA para la Salud — Hackathon Gemma 4 × UNER

## Encuentros preparatorios

*Para prepararte, aprender y comenzar a crear*

- **16 JUL** — Encuentro 1 · Inmersión
- **23 JUL** — Encuentro 2 · Hands-on técnico

100% virtuales por Google Meet · 18:00 h · Abiertos y gratuitos para toda la comunidad · Facultad de Ingeniería, UNER


---

# ENCUENTRO 1 · 16 JULIO

## Inmersión

Qué es Build with Gemma · Conocé Gemma 4 · Reglas del hackathon · Ideas y equipos


---

## Una hora, cuatro paradas

*Encuentro 1 · Lo que vamos a ver hoy*

1. **¿Qué es Build with Gemma?** — La iniciativa, el hackathon y por qué IA para la salud.
2. **Conocé Gemma 4** — La familia de modelos y dónde corre cada una.
3. **Reglas del hackathon** — Cómo se entrega, cómo se juzga, qué NO hacer.
4. **Ideas y formación de equipos** — El menú de proyectos y cómo armar un buen equipo.

Es un encuentro de inmersión: amplio a propósito. La parte técnica pesada es el 23 de julio.


---

## Diez años de IA médica que tiene que funcionar de verdad

*Quién les habla (y dónde me pueden discutir)*

1. **Histora** — CTO y co-fundador. Historia clínica dental con IA. HIPAA/GDPR, anonimización DICOM, FHIR.
2. **APN Health** — IA cardíaca. Completación de forma 3D de aurícula izquierda. Dice 0.954, HD95 3.0 mm.
3. **EvolvingAgentsLabs** — Infraestructura open-source de agentes: skills, memoria, runtime local.
4. **Antes** — Navegación quirúrgica de rodilla, ML en el borde (Android), documentación clínica por voz.

Voy a ser mentor y jurado del hackathon. Nada de lo que muestro es teórico: lo cobré, lo rompí, o lo tuve que arreglar.


---

## ¿Qué es Build with Gemma?

*Parada 1*

- **La iniciativa** — Google abre su familia de modelos Gemma para que cualquiera construya con ellos. El «Gemmaverse» ya superó los 160 millones de descargas y una docena de modelos especializados.
- **Nuestro hackathon** — El mandato es uno solo: hacer algo útil o creativo con Gemma 4 haciendo trabajo real en el corazón del proyecto. Formas de arrancar, varias gratuitas: Google AI Studio, Colab, Ollama, AI Edge.
- **IA para la Salud** — El tema no es decorativo. Es el que hace que los modelos abiertos dejen de ser «la opción barata» y pasen a ser la única viable.
- **Entrega final en Kaggle** — Writeup + demo + submission.

*Fuente: iniciativa Build with Gemma / Gemma 4 Challenge (Google). Verificá las reglas específicas del hackathon UNER en el Kaggle del flyer.*


---

## El dato clínico no sale del edificio.

*Por qué este tema, y por qué modelos abiertos*

Lo que te obliga:

- **GDPR Art. 9** — datos de salud = categoría especial
- **HIPAA** — PHI, BAA, auditoría de accesos
- **Ley 25.326** — datos sensibles (Argentina)
- **EU AI Act** — IA médica = alto riesgo

En salud, el modelo abierto no es «la opción barata». Es la única arquitectura legalmente viable, porque el dato no puede irse a un tercero.

**Si el dato tiene que salir a la API de un tercero para que el modelo funcione, el proyecto no existe. No es más caro: es inviable.**


---

## Cinco variantes, un mismo modelo base

*Parada 2 · Gemma 4 · Abril 2026 · Apache 2.0*

| Variante | Dónde corre | Memoria |
|---|---|---|
| **E2B** | Celular, Pi, browser | < 1.5 GB RAM/VRAM |
| **E4B** | Edge y agentes. El sweet spot. | < 1.5 GB RAM/VRAM |
| **12B** | Laptop. Sin encoders. | 16 GB RAM/VRAM |
| **26B A4B** | MoE: 26B cargados, 4B activos. | GPU RAM/VRAM |
| **31B** | Denso. Servidor. | ~19 GB RAM/VRAM |

Todas: multimodales · 140+ idiomas · thinking mode · rol «system» nativo · function calling nativo · Apache 2.0

Hoy solo tienen que llevarse una intuición: **se elige el tamaño según el hardware.** La mecánica fina (PLE, MoE) la vemos el 23.


---

## El 12B no tiene encoders multimodales

*El highlight para bioingeniería*

Un modelo multimodal clásico traduce imagen y audio con encoders separados antes de pasarlos al LLM. Eso agrega latencia y memoria.

- **Tradicional:** Imagen → encoder → LLM · Audio → encoder → LLM (+ latencia, + memoria)
- **Gemma 4 12B · unificado:** Imagen y audio → **proyección lineal** → LLM backbone (16 GB · corre en tu laptop)

El audio crudo se proyecta al mismo espacio dimensional que los tokens de texto. Para bioingenieros con background en señales, esto es un tema de charla en sí mismo.


---

## El mismo modelo, tres lugares donde corre

*Conocé Gemma 4, en concreto · Demo por pantalla compartida*

1. **COLAB** — Gratis · GPU T4. E4B con Transformers. Cero fricción, cero hardware, cero excusas.
2. **TU LAPTOP** — Ollama · 12B. Le tiro una imagen. Le tiro un audio de dictado. Encoder-free: audio nativo.
3. **TU CELULAR** — AI Edge Gallery · E4B. Modo avión. Y sigue funcionando. Multimodal, offline, US$300.

Remoto: el modo avión del celular se muestra espejando la pantalla del teléfono en Meet. Truco escénico único — y prueba de que el dato no salió del bolsillo.


---

## Benchmark ≠ utilidad clínica.

*Antes de que se enamoren del modelo*

- **Un modelo al 69% en MedQA no es un médico al 69%.** Falla de formas que un médico jamás falla. No se olvida de que existe la anatomía.
- **Contaminación de datos.** Pudo ver el benchmark en el pretraining. La doc oficial recomienda validar sobre datos NO públicos.
- **La alucinación en medicina no es un bug gracioso.** Es un evento adverso. Y la responsabilidad legal es del que despliega, no del que entrena.

En el Encuentro 2 lo vamos a ver romperse en vivo, con un caso médico con datos contradictorios.


---

## El menú: cada tarjeta es un proyecto

*Parada 4 · Ideas para su proyecto*

Modelos médicos abiertos, ya entrenados en dominio. Sirven como punto de partida — el trabajo real es de ustedes.

- **Imagen 3D** — Volúmenes de CT y MRI completos. Primer modelo abierto que lo hace.
- **Histopatología WSI** — Whole-slide interpretado por parches. +47% macro F1.
- **Localización anatómica** — Bounding boxes en Rx de tórax. IoU 3% → 38%.
- **Longitudinal** — Rx comparada contra estudios previos del paciente.
- **Documentos y EHR** — Extracción de informes de lab. EHRQA 68% → 90%.
- **MedASR — dictado** — 58% menos errores que Whisper large-v3 en tórax.

MedGemma se rige por los Health AI Developer Foundations terms, no por Apache. Y sigue siendo base Gemma 3: **fine-tunear Gemma 4 al dominio médico es un hueco abierto = una tesis.**


---

## Un buen equipo tiene estos cinco roles

*Formación de equipos*

No hace falta que sean cinco personas. Sí hace falta que alguien se haga cargo de cada rol.

1. **Datos** — Consigue, limpia y etiqueta. Es el 80% del trabajo. Sin datos no hay proyecto.
2. **Modelo** — Corre Ollama, hace el fine-tuning con Unsloth, arma el pipeline de inferencia.
3. **Evaluación** — Define la métrica correcta y mide baseline vs. resultado. Sin esto, es una demo.
4. **Dominio / clínica** — Un bioingeniero o alguien de salud que diga si el problema y la salida tienen sentido.
5. **Writeup y demo** — Cuenta la historia y arma la entrega de Kaggle. Un gran proyecto mal contado pierde.

Busquen complementariedad, no cinco personas que sepan lo mismo. **El equipo con un clínico adentro tiene una ventaja injusta.**


---

## Cómo los voy a juzgar (no es secreto)

*Parada 3 · Reglas del hackathon*

- **30% — ¿Midieron algo?** Baseline y número después. Sin evaluación no hay proyecto, hay demo.
- **25% — ¿El dato está protegido?** PHI a una API de terceros = muerto por diseño.
- **25% — ¿Corre?** En vivo, en su máquina. No un video, no un slide.
- **20% — ¿Saben dónde falla?** Si dicen que funciona siempre, no lo probaron. Muéstrenme el caso que rompe.

**NO puntúo:** el tamaño del modelo · la cantidad de features · lo lindo que quedó el frontend.

Y un piso innegociable: **nada de esto es un dispositivo médico.** El EU AI Act lo clasifica alto riesgo. Anonimicen antes de tocar nada.


---

## Tarea para el 23 de julio

*Cierre Encuentro 1*

El Encuentro 2 es un taller. Van a tipear ustedes. Sin esto listo, no lo van a poder seguir.

- ✓ **Instalar Ollama** — `ollama run gemma4:e4b` — anda sin GPU también, más lento.
- ✓ **Instalar AI Edge Gallery** — Y descargar E2B o E4B adentro de la app.
- ✓ **Crear cuenta en Kaggle** — Es donde se entrega. Únanse al hackathon desde ya.
- ✓ **Empezar a pensar el equipo** — Traigan una idea del menú, o una propia. Hablamos en el taller.

**Nos vemos el 23 · 18:00 h · por Google Meet · Encuentro 2: Hands-on técnico**


---

# ENCUENTRO 2 · 23 JULIO · TALLER

## Hands-on técnico

Ollama + Unsloth · Function calling y multimodalidad · Feedback · Entrega


---

## Cuatro bloques, manos en el teclado

*Encuentro 2 · Lo que vamos a hacer hoy*

1. **Taller práctico (Ollama + Unsloth)** — Correr Gemma 4 local y fine-tunear con QLoRA.
2. **Function calling y multimodalidad** — Skills en vivo, agentes, imagen y audio.
3. **Feedback de proyectos** — Los errores que voy a marcar, y cómo evitarlos.
4. **Preparación de la entrega** — Writeup, demo y submission a Kaggle.

Espeja los cuatro temas anunciados. Si no instalaron nada el 16, siéntense con alguien que sí.


---

## «Efectivo» y «activo» no son lo mismo

*Bloque 1 · Taller práctico — elegir el tamaño*

**E — La E de E2B / E4B (Per-Layer Embeddings)**
«E» = parámetros efectivos, no totales. Cada capa del decoder tiene su embedding chico por token, usado solo como lookup. Los pesos estáticos ocupan más de lo que sugiere el nombre. No es un bug.

**A — La A de 26B A4B (Mixture of Experts)**
Activa 4B por token, pero carga los 26B en memoria. Corre casi como un 4B, ocupa casi como un 26B denso. El trade-off es velocidad a cambio de memoria. No es magia.

En el taller: `ollama run gemma4:e4b`. **Elegir bien el tamaño es la primera decisión de ingeniería del hackathon.**


---

## Dos ejes de especialización

*El concepto que ordena todo el taller*

**A — ADAPTER · Cambiás el modelo**
LoRA / QLoRA. Pesos nuevos. Jerga, formato, estilo, clasificación. Requiere datos y GPU. Vive en la GPU, no en el celular.

**S — SKILL · Cambiás las herramientas**
Un SKILL.md de texto plano. Buscar, consultar, dibujar, llamar otro modelo. Cero entrenamiento, cero GPU. Corre en el celular, offline.

**Adapter en la GPU. Skill en el borde.** Si se llevan un solo concepto del taller, que sea este.


---

## Function calling nativo · 6 tokens especiales

*Bloque 2 · Function calling y multimodalidad*

No es prompt engineering. El modelo fue entrenado sabiendo cuándo llama una herramienta.

1. **SKILL.md abierto** — Estándar de agentskills.io, el mismo que usa Claude. No es propietario.
2. **El modelo decide** — Qué tool, en qué orden, cómo componer. Autónomo.
3. **On-device** — ~4.000 tokens con 2 skills en < 3 s. Sin internet.
4. **Prompt bloat → capacidad** — Cargás la capacidad que necesitás, no un system prompt gigante.

**DEMO EN VIVO** · escribimos una SKILL.md de cero → foto de etiqueta de lab → JSON, en el celular


---

## La capacidad es del modelo. El soporte es del runtime.

*Los dos gotchas que les van a costar horas*

**vLLM · function calling** — Si no habilitás thinking en el chat template, el agente NO llama herramientas. Y no vas a entender por qué. `enable_thinking: true` — prende razonamiento **Y** function calling.

**El modelo grande no es el mejor agente** — E4B: sweet spot. ~22 s simples, ~2,5 min complejas. 26B / 31B: demasiado lentos para loops multi-roundtrip. La latencia se multiplica por cada ida y vuelta.

**Lección general para toda la carrera: cuando algo no anda, chequeen el runtime antes de culpar al modelo.**


---

## LoRA en noventa segundos

*Bloque 1 · Taller — Unsloth*

`y = x·W + x·A·B` — **W** base congelado · **A·B** adapter entrenable, rango bajo

- **0,2 – 1%** de los parámetros se entrenan
- **30 – 100 MB** pesa un adapter a rango 16
- **< 1%** de cómputo extra por capa (r=16)

El base nunca se toca. Por eso podés tener muchos adapters sobre un mismo base — y por eso el multi-LoRA funciona.

**QLoRA** = base en 4 bits (NF4). ~90% de la calidad de LoRA, en la mitad de la memoria.


---

## ¿Entra en tu placa? Casi seguro que sí

*Números reales · Fuente: documentación de Unsloth*

| Configuración | VRAM (GB) |
|---|---|
| E2B entrenar | 8.0 |
| E4B entrenar | 10.0 |
| RL | 9.0 |
| E4B LoRA | 17.0 |
| 31B QLoRA | 22.0 |
| 26B-A4B LoRA | 42.0 |

**Traducción:**

- La T4 gratis de Colab (16 GB) alcanza para E4B en QLoRA.
- Una RTX 3060 (12 GB) alcanza para E2B y E4B.
- Unsloth: ~1,5× más rápido, ~60% menos VRAM que FA2, sin perder precisión.
- Mejor E4B en QLoRA que E2B en LoRA: la pérdida por cuantizar es despreciable.

**«No tengo GPU» dejó de ser una excusa válida. Ahora la excusa tiene que ser sobre los datos.**


---

## Cuatro trampas del fine-tuning

*Los errores que van a cometer a las 3 AM*

1. **MoE + 4 bits = mal** — El routing del 26B-A4B y la cuantización 4-bit interactúan pésimo. Usá LoRA 16-bit. → `load_in_16bit`
2. **El rol es «model»** — No «assistant». Silencioso y letal: entrena mal y te enterás en la evaluación. → `role: "model"`
3. **Perdiste el razonamiento** — Mezclá ≥75% de ejemplos con reasoning para preservar el thinking mode. → `≥ 75% reasoning`
4. **Anda en Colab, rompe en Ollama** — Causa #1: chat template mismatch entre entrenamiento e inferencia. → verificá el template

**Bonus:** si ven un loss de 13-15 en E2B/E4B, es NORMAL. Quirk de los multimodales. No lo arreglen.


---

## ¿Fine-tuning o RAG? Y qué esperar

*Antes de encender la GPU*

**El resultado a esperar:**

| | Accuracy |
|---|---|
| Base | 33.0 |
| Fine-tuneado (1 época) | 89.0 |

MedGemma 4B sobre MRI cerebral · LoRA · 1 época · dataset chico → **+56 puntos**

- ✓ **Fine-tuneá para:** formato consistente (JSON, FHIR) · jerga de dominio, clasificación propia · menos latencia.
- ✕ **NO fine-tunees para:** conocimiento nuevo (→ RAG) · datos que cambian · lo que un buen prompt ya resuelve.

**Regla de hackathon: 80% datos + evaluación, 20% modelo.** El notebook oficial con RL va de 14→70% pero pide A100 40GB y 11 h: no es de fin de semana.


---

## «Un E4B fine-tuneado iguala a un 31B prompteado.»

*Lo que no está probado*

Lo van a leer en cinco blogs. **No está en ningún benchmark revisado.** Díganlo como hipótesis, no como hecho.

**Lo que SÍ es defendible:**
LoRA Land (310 modelos fine-tuneados): 301 de 310 superaron a su base, y 224 de 310 superaron a GPT-4 en su tarea específica. Un modelo chico especializado le gana a un gigante generalista — **en esa tarea, y solo en esa.**


---

## Un solo Gemma. Muchos especialistas encima.

*La síntesis · La arquitectura de su proyecto*

**BASE:** Gemma 4 E4B — cargado UNA vez, ~4 GB en VRAM, `vLLM --lora-modules`
**ROUTER:** el agente elige el adapter por request

Adapters (~60 MB cada uno):

- Extracción de labs
- Notas periodontales
- QA sobre FHIR
- Dictado clínico

Sub-ms de swap por request · ~200 adapters en una A100 con <5% de latencia · en GPU (no en el Gallery: en el borde la especialización es la skill).


---

## Los siete errores que voy a marcar

*Bloque 3 · Feedback de proyectos*

1. **Data leakage a nivel de paciente** — Cortes del mismo paciente en train y test. Accuracy inflada que no ves. El error #1.
2. **Sin baseline** — Un número solo no es un resultado. Necesito el antes y el después.
3. **PHI en una API de terceros** — Muerte instantánea, por más que funcione bien.
4. **Métrica equivocada** — Accuracy sobre datos desbalanceados no dice nada. Quiero F1, AUC o sensibilidad/especificidad.
5. **Demo grabada** — Si no corre en vivo, no corre.
6. **Chat template mismatch** — Funciona en el notebook, se rompe en la app. Clásico.
7. **«El modelo dijo X» = «X es verdad»** — No. El modelo dijo X. Eso es todo lo que sabés.

**Traigan a la sesión de feedback: su baseline, su métrica, y el caso donde su proyecto falla.** Con eso les doy feedback útil en 3 minutos.


---

## Writeup, demo y Kaggle

*Bloque 4 · Preparación de la entrega*

**Writeup**

- El problema y por qué importa.
- Los datos: origen, tamaño, cómo se dividieron.
- Baseline vs. resultado, con la métrica correcta.
- Dónde falla y qué haría con más tiempo.

**Demo**

- Corre en vivo, no grabada. Menos de 3 minutos.
- Muestra el caso feliz Y el caso que rompe.
- El dato nunca sale a un tercero.

**Kaggle**

- Submission según las reglas del hackathon.
- Notebook reproducible, con seeds.
- Modelo y licencia declarados.
- Después: MedGemma Impact Challenge, US$100K.

**Licencia — decilo antes de publicar: Gemma 4 es Apache 2.0. MedGemma NO (Health AI Developer Foundations terms).**


---

# El modelo es lo fácil.

## Los datos, la evaluación y la regulación son el trabajo.

**Ahora vayan y construyan algo.**

Nos vemos en el hackathon · Consultas: ciev.ingenieria@uner.edu.ar

