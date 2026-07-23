# Guion — Gemma 4 en la UNER
### Dos charlas de una hora · Facultad de Ingeniería, Oro Verde · Previo al hackathon

---

## Cómo usar este documento

Cada slide tiene cuatro bloques:

- **⏱ Tiempo** — minuto de inicio y duración objetivo.
- **🎙 Qué decir** — no es un texto para leer. Es el argumento, en el orden en que tiene que salir.
- **📎 Fuente** — de dónde sale cada número. Si un alumno te lo discute, tenés dónde pararte.
- **⚠ Riesgo / Nota** — lo que puede salir mal, o lo que hay que verificar antes.

**Regla general de las dos charlas:** ningún dato duro sale de tu memoria. Sale de una fuente citada. Cuando no hay fuente sólida, lo decís explícitamente como hipótesis. Eso es lo que te separa de un charlista de producto.

---

## ⚙️ Checklist previo (hacer 48 h antes, no la mañana de)

| ✓ | Ítem |
|---|---|
| ☐ | Pesos descargados: `gemma4:12b` y `gemma4:e4b` en Ollama. **Verificar el tag exacto** con `ollama list` — el naming cambió entre releases. |
| ☐ | AI Edge Gallery instalado en el celular, con E4B ya descargado **adentro de la app**. |
| ☐ | La skill `lab-label-extractor` ya importada y probada en el Gallery. |
| ☐ | Los tres notebooks abiertos en pestañas de Colab, **ya ejecutados una vez** (para que el caché de HF esté caliente). |
| ☐ | Video de backup de cada demo (30–60 s cada uno, grabados con OBS o el grabador de pantalla del celular). |
| ☐ | Imagen de prueba: una radiografía panorámica o una etiqueta de laboratorio, en el escritorio, con nombre corto. |
| ☐ | Audio de prueba: 15 s de dictado clínico grabado por vos, en `.wav`. |
| ☐ | Adaptador HDMI. Sí, ese. |
| ☐ | **Asumir que no hay wifi.** Todo lo que dependa de internet tiene que tener plan B. |

---
---

# CHARLA 1
## "Un modelo, cuatro tamaños, cuatro lugares donde corre"

**Objetivo de la hora:** que se vayan con el entorno instalado y con un modelo mental correcto para elegir tamaño de modelo según hardware. Nada más. Si logran eso, la charla 2 vuela.

---

### SLIDE 1 — Portada
**⏱ 0:00 · 1 min**

**🎙 Qué decir**

> "Buenas. Son dos encuentros de una hora. El primero es sobre dónde corre esto. El segundo es un taller, con las laptops abiertas.
>
> El título de la serie no es 'Google sacó un modelo nuevo'. Es lo que dice el subtítulo: **datos que no salen del edificio**. Si se llevan una sola idea de las dos horas, quiero que sea esa."

**⚠ Nota:** no arranques con tu CV. Arrancá con la tesis. El CV viene en la slide siguiente, y solo para justificar por qué te pueden creer.

---

### SLIDE 2 — Quién habla
**⏱ 0:01 · 2 min**

**🎙 Qué decir**

> "Cuatro cosas, rápido, para que sepan de dónde vengo y para que sepan **dónde pueden discutirme**.
>
> **Histora**: soy CTO y co-fundador. Historia clínica dental con IA. Trabajo todos los días con HIPAA y GDPR, con anonimización de DICOM y con interoperabilidad FHIR. Eso significa que la parte regulatoria de estas charlas no es teoría que leí — es el motivo por el que a veces no duermo.
>
> **APN Health**: contrato de IA cardíaca. Un modelo de completación de forma 3D de aurícula izquierda a partir de nubes de puntos ralas de un catéter. Dice de 0.954, HD95 de 3 milímetros.
>
> **EvolvingAgentsLabs**: infraestructura open-source de agentes. Skills, memoria, runtime local. De ahí sale la mitad de la charla 2.
>
> **Antes**: navegación quirúrgica de rodilla, inferencia en el borde con LiteRT en Android, documentación clínica por voz.
>
> El punto no es el currículum. El punto es que puedo decirles **cuál es la diferencia entre un Dice de 0.954 y un producto**. Son dos años de diferencia."

**⚠ Nota:** decilo en 2 minutos exactos. Si te extendés, perdés el aula.

---

### SLIDE 3 — Divider Charla 1
**⏱ 0:03 · 30 s**

**🎙 Qué decir**

> "Charla 1. Terminan con Ollama y AI Edge Gallery instalados. Ese es el único KPI."

---

### SLIDE 4 — La tesis
**⏱ 0:03 · 5 min** ← *no la apures, es el frame de todo*

**🎙 Qué decir**

> "Esta es la tesis de las dos charlas.
>
> **El dato clínico no sale del edificio.**
>
> En cualquier otro dominio, elegir entre un modelo abierto y uno cerrado es una decisión de costo o de rendimiento. En salud, no. En salud es una decisión de **si el proyecto puede existir legalmente o no**.
>
> Miren la columna de la derecha:
> - **GDPR, artículo 9**: los datos de salud son categoría especial. Requieren base legal explícita.
> - **HIPAA**: PHI, Business Associate Agreements, auditoría de todos los accesos.
> - **Ley 25.326** en Argentina: datos sensibles.
> - **EU AI Act**: la IA médica está clasificada como sistema de alto riesgo.
>
> Traducción práctica: si el dato tiene que salir a la API de un tercero para que tu modelo funcione, **tu proyecto no existe**. No es que es más caro. No es que es más lento. Es que no lo podés desplegar.
>
> Y ahí es donde los modelos abiertos dejan de ser 'la opción barata' y pasan a ser **la única arquitectura viable**.
>
> Yo esto no lo aprendí leyendo. Lo aprendí diseñando el pipeline de anonimización de Histora: anonimizar, borrar el original, archivar, verificar, borrar el anonimizado. Cada paso de ese orden está ahí porque si lo invertís, violás algo."

**📎 Fuente**
- GDPR Art. 9 — categorías especiales de datos personales (datos relativos a la salud).
- EU AI Act — la IA médica se clasifica como sistema de alto riesgo. Consultoras que asesoran en integración de MedGemma en la UE lo mencionan explícitamente junto con MDR/IVDR y la recomendación de self-hosting para datos de pacientes.
- Ley 25.326 (Argentina), art. 2 y 7 — datos sensibles.

**💡 Ejemplo concreto para tirar acá**

> "Un ejemplo real: en Histora tuvimos que decidir si anonimizábamos DICOM a nivel de instancia o a nivel de estudio. Parece un detalle técnico. No lo es: si anonimizás instancia por instancia, perdés la trazabilidad del estudio y rompés la posibilidad de comparar longitudinalmente. Esa decisión de arquitectura salió de leer la regulación, no de leer un paper."

---

### SLIDE 5 — El mapa de la familia
**⏱ 0:08 · 6 min**

**🎙 Qué decir**

> "Gemma 4. Salió en abril de 2026. Apache 2.0 — comercialmente permisiva, sin las restricciones raras de las licencias anteriores de Gemma.
>
> **Cinco variantes. Y no es la grilla de Gemma 3**, así que si vienen con el modelo mental viejo, tírenlo.
>
> - **E2B y E4B** — la 'E' es de *efectivo*, ya vamos a ver por qué. Corren en celular, en Raspberry Pi, en el browser. Bajo 1,5 GB de RAM. 128K de contexto.
> - **12B** — el unificado, sin encoders. Corre en una laptop con 16 GB. Audio nativo. Es la joya, y le dedico una slide entera.
> - **26B A4B** — Mixture of Experts. 26 mil millones de parámetros cargados, 4 mil millones activos por token.
> - **31B** — denso. Servidor o workstation.
>
> Todas: multimodales, más de 140 idiomas, thinking mode configurable, soporte nativo del rol `system` — que Gemma 3 no tenía — y **function calling nativo**.
>
> El objetivo de esta slide no es que memoricen la tabla. Es que salgan de acá sabiendo **elegir el tamaño según el hardware que tienen**. Esa es la decisión de ingeniería real, y es la que van a tomar el viernes a la noche del hackathon."

**📎 Fuente**
- Documentación de Google AI for Developers (`ai.google.dev/gemma/docs/core`): cuatro arquitecturas — small sizes (E2B/E4B) para móvil/edge/browser, un denso de 31B, un MoE de 26B, y un unificado de 12B encoder-free. Cinco tamaños: E2B, E4B, 12B, 31B, 26B A4B.
- Model card en Hugging Face (`google/gemma-4-31B-it`): contexto hasta 256K, 140+ idiomas, thinking mode configurable, soporte nativo del rol `system`, atención híbrida (sliding window local intercalada con global, con la última capa siempre global), unified KV en las capas globales y Proportional RoPE.
- Contexto: 128K en E2B/E4B, 256K en 26B A4B / 31B.
- Licencia Apache 2.0 — blog de Google, lanzamiento de Gemma 4.

**⚠ Nota:** *no* prometas números de benchmark de memoria exactos sin verificar. La tabla oficial de memoria advierte que los números cambian según el motor de inferencia y el entorno.

---

### SLIDE 6 — PLE y MoE
**⏱ 0:14 · 6 min** ← *acá se separan los que entienden de los que repiten*

**🎙 Qué decir**

> "Dos conceptos. Si no los entienden, van a elegir mal el modelo y van a culpar a la GPU.
>
> **La E de E2B y E4B: Per-Layer Embeddings.**
>
> 'E' es de *parámetros efectivos*, no totales. En vez de agregar más capas al modelo, PLE le da a **cada capa del decoder su propio embedding chiquito para cada token**. Esas tablas de embeddings son grandes, pero solo se usan como lookup rápido — no participan del cómputo pesado.
>
> ¿Consecuencia práctica? **Los pesos estáticos ocupan más memoria de lo que sugiere el nombre.** Si ven que un 'E4B' pesa más de lo que esperaban, no es un bug. Es PLE.
>
> **La A de 26B A4B: Mixture of Experts.**
>
> Activa solo 4 mil millones de parámetros por token durante la generación. **Pero los 26 mil millones tienen que estar TODOS en memoria**, porque si no, el routing entre expertos se hace lento.
>
> O sea: corre casi tan rápido como un 4B, pero ocupa casi como un 26B denso.
>
> Ese trade-off **es el punto**. No es magia. Es velocidad a cambio de memoria. Y es una decisión de ingeniería que ustedes van a tener que tomar."

**📎 Fuente**
- `ai.google.dev/gemma/docs/core`: "The 'E' stands for 'effective' parameters. The smaller models incorporate Per-Layer Embeddings (PLE)... Rather than adding more layers to the model, PLE gives each decoder layer its own small embedding for every token. These embedding tables are large but only used for quick lookups, which is why the total memory required to load static weights is higher than the effective parameter count suggests."
- Misma fuente sobre MoE: "While it only activates 4 billion parameters per token during generation, all 26 billion parameters must be loaded into memory to maintain fast routing and inference speeds. This is why its baseline memory requirement is much closer to a dense 26B model than a 4B model."

**💡 Pregunta para tirarle al aula (los despierta)**

> "Pregunta: si el MoE activa solo 4B por token pero carga 26B, ¿en qué escenario conviene sobre el 31B denso? …Exacto: cuando tenés memoria pero necesitás throughput. Cuando la memoria es el cuello de botella, el MoE no te sirve de nada."

---

### SLIDE 7 — El 12B encoder-free
**⏱ 0:20 · 6 min** ← *tu audiencia es de bioingeniería: esto les va a encantar*

**🎙 Qué decir**

> "Esta es, para ustedes específicamente, la parte más interesante de todo Gemma 4.
>
> Un modelo multimodal tradicional tiene **encoders separados**: un encoder de visión que traduce la imagen a embeddings, un encoder de audio que hace lo mismo con el sonido, y recién ahí eso entra al LLM. Eso agrega latencia y agrega memoria.
>
> Gemma 4 12B **no tiene encoders multimodales**.
>
> - **Visión**: reemplazaron el encoder de visión por un módulo de embedding liviano — una sola multiplicación de matrices, embedding posicional y normalizaciones. El backbone del LLM se hace cargo del procesamiento visual.
> - **Audio**: eliminaron el encoder de audio por completo. **Proyectan la señal de audio cruda directamente al mismo espacio dimensional que los tokens de texto.**
>
> Paren un segundo en eso. Ustedes son bioingenieros. Muchos vienen de procesamiento de señales. Lo que están diciendo es que una proyección lineal de la señal cruda al espacio de tokens **alcanza** para que el modelo entienda audio.
>
> Eso es o bien una idea muy elegante, o bien una afirmación que merece que la interroguen. Yo creo que es lo primero, pero quiero que salgan de acá pensando en la segunda.
>
> Resultado práctico: **16 GB de VRAM o memoria unificada**. Corre en su laptop. Y el rendimiento se acerca al del 26B con menos de la mitad de la huella de memoria."

**📎 Fuente**
- Blog de Google, "Introducing Gemma 4 12B: a unified, encoder-free multimodal model" (junio 2026): "We replaced Gemma 4's vision encoder with a lightweight embedding module consisting of a single matrix multiplication, positional embedding and normalizations." / "We removed the audio encoder entirely and projected the raw audio signal into the same dimensional space as text tokens."
- Misma fuente: "Small enough to run locally with just 16GB of VRAM or unified memory." / "Benchmark performance nearing our 26B model."
- Misma fuente: primer modelo de tamaño medio de la familia con entrada de audio nativa. Los modelos Gemma 4 superaron los 150 millones de descargas.

**💡 Momento de conexión con la audiencia**

> "Piensen lo que esto habilita: dictado clínico → modelo → nota estructurada, **sin un pipeline de ASR separado**. Un solo modelo. Corriendo en la máquina del consultorio. Sin que el audio del paciente salga jamás."

---

### SLIDE 8 — La escalera (DEMO EN VIVO)
**⏱ 0:26 · 20 min** ← *el corazón de la charla. NO lo apures.*

**🎙 Estructura de la demo**

#### Peldaño 1 — Colab (5 min)
> "Abro Colab. GPU T4, que es gratis. Cargo E4B con Transformers. No tengo que bajar nada a mi máquina, no tengo que tener GPU, no tengo excusa."

→ Abrir `notebooks/01_gemma4_escalera.ipynb`, celda de texto. Correr un prompt. Mostrar que anda.

> "Esto es el piso. Si alguien en este aula me dice que no puede probar Gemma 4 porque no tiene hardware, le muestro esta pestaña."

#### Peldaño 2 — Tu laptop, Ollama, 12B (8 min)
> "Ahora bajo un escalón hacia mi máquina. Ollama. Gemma 4 12B."

```bash
ollama run gemma4:12b
```

> "Le tiro una imagen."

→ Arrastrar la radiografía / imagen intraoral. Pedir descripción estructurada.

> "Y ahora — esto es lo que ningún otro modelo de este tamaño hace bien — **le tiro un audio**."

→ Pasar el `.wav` de dictado. Pedir extracción estructurada.

> "Un modelo. Una máquina. Imagen y audio. Cero encoders. Cero internet."

#### Peldaño 3 — El celular (7 min) ← **EL MOMENTO**
> "Último escalón. Mi teléfono."

→ Abrir AI Edge Gallery. E4B cargado.

> "Y ahora hago lo único importante de toda la charla."

→ **Poner el teléfono en modo avión. Mostrar el ícono de avión en la pantalla proyectada.**

→ Seguir prompteando. Pasarle una foto tomada en ese momento.

> "Multimodal. Offline. En un aparato de trescientos dólares. Sin que un solo byte salga de este dispositivo.
>
> **Ahora vuelvan a la slide de la tesis, mentalmente.** ¿Se acuerdan de 'el dato clínico no sale del edificio'? Acá el dato no salió ni del bolsillo."

**📎 Fuente**
- E2B/E4B corren bajo 1,5 GB de RAM en dispositivos de gama media a alta. El runtime LiteRT-LM procesa ~4.000 tokens a través de dos Agent Skills en menos de tres segundos.
- Google AI Edge Gallery está disponible en iOS y Android y permite experimentar con IA que corre enteramente on-device.
- Ollama tiene soporte desde el día uno.

**⚠ Riesgos de esta slide (los más altos de la charla)**
1. **El wifi de la facultad.** Todo tiene que estar precargado. El Colab debe estar ya ejecutado.
2. **El espejado del celular.** Probalo el día anterior, con el cable y el proyector reales. Si falla, tenés el video.
3. **La latencia del 12B en tu laptop con el proyector conectado** puede ser peor de lo que esperás (el proyector consume GPU). Bajá a `e4b` si hace falta y decilo en voz alta: "miren, con el proyector conectado el 12B se arrastra — esto también es información útil".

---

### SLIDE 9 — Anti-hype
**⏱ 0:46 · 8 min**

**🎙 Qué decir**

> "Esta es la slide que nadie más les va a mostrar, y es la más importante desde el punto de vista ético.
>
> **Benchmark no es igual a utilidad clínica.**
>
> Uno: un modelo que saca 69% en MedQA **no es un médico al 69%**. Es un sistema que falla de formas que un médico nunca falla. Un médico no se olvida de que existe la anatomía. Un modelo sí.
>
> Dos: **contaminación de datos**. El modelo pudo haber visto el benchmark durante el pretraining. La documentación oficial de MedGemma lo dice explícitamente: recomiendan validar sobre datasets que **no** son públicos, justamente por eso.
>
> Tres, y este es el que importa: **la alucinación en medicina no es un bug gracioso. Es un evento adverso.** Y la responsabilidad legal es del que despliega, no del que entrena.
>
> Ahora se los muestro."

→ **DEMO DEL FALLO.** Prompt preparado de antemano donde el modelo alucina con confianza total sobre algo médico.

> "¿Vieron el tono? No dudó. No dijo 'no estoy seguro'. Esa **confianza sin calibración** es el problema real de estos sistemas, y es el problema que ustedes van a tener que resolver."

**📎 Fuente**
- Model card de MedGemma: "Data contamination concerns: ...there is a risk of data contamination, where the model might have inadvertently seen related medical information during its pre-training, potentially overestimating its true ability to generalize... Developers should validate MedGemma on datasets not publicly available."
- MedGemma 1.5 4B saca 69% en MedQA (subió de 64% en MedGemma 1).
- Disclaimer oficial de DeepMind: "The outputs generated by these models are not intended to directly inform clinical diagnosis, patient management decisions, treatment recommendations, or any other direct clinical practice applications."

**💡 Cómo preparar el fallo (hacelo esta semana)**
Probá prompts de este estilo hasta que uno rompa bien:
- Pedile que interprete una imagen médica **rotada o invertida** y ver si detecta la orientación.
- Pedile un valor de referencia de laboratorio de una unidad poco común y ver si lo inventa.
- Pedile que compare dos radiografías donde una está **duplicada** y ver si "encuentra" diferencias.
- Dale un caso clínico con un dato internamente contradictorio y ver si lo señala o si lo racionaliza.

El cuarto es el mejor: mide si el modelo **detecta inconsistencias** o si las suaviza. Los modelos suelen suavizar. Eso es letal en clínica.

---

### SLIDE 10 — Tarea
**⏱ 0:54 · 5 min + preguntas**

**🎙 Qué decir**

> "Tarea. No es opcional. Si llegan a la charla 2 sin esto, **la charla 2 no existe para ustedes**, porque es un taller y van a tipear ustedes.
>
> Uno: instalar Ollama y correr `ollama run gemma4:e4b`. Anda sin GPU también, más lento.
> Dos: instalar AI Edge Gallery desde el repo de google-ai-edge, y **descargar el modelo adentro de la app**. Eso último es lo que se olvidan.
> Tres: abrir el cookbook de Gemma y correr un notebook cualquiera en Colab. Que arranque, nada más.
>
> Vengan con las máquinas listas y la batería cargada. Preguntas."

**📎 Enlaces a proyectar**
- `github.com/google-ai-edge/gallery`
- `github.com/google-gemma/cookbook`
- `ollama.com/library/gemma4`

---
---

# CHARLA 2
## "Un Gemma, muchos Gemmas"

**Objetivo de la hora:** que se vayan con (a) una skill funcionando en su celular, (b) el modelo mental de adapter-vs-skill, y (c) la arquitectura multi-LoRA como plano de su proyecto de hackathon.

**Formato: TALLER.** Laptops abiertas. Vos tipeás, ellos tipean.

---

### SLIDE 11 — Divider Charla 2
**⏱ 0:00 · 1 min**

**🎙 Qué decir**

> "Laptops abiertas. Esto no es una charla, es un taller. Si no instalaron nada, siéntense al lado de alguien que sí."

---

### SLIDE 12 — Los dos ejes
**⏱ 0:01 · 7 min** ← *el concepto más valioso de todo el taller*

**🎙 Qué decir**

> "La tesis de esta hora. Hay **dos ejes de especialización**, son ortogonales, y todo el mundo los confunde.
>
> **Eje 1: el ADAPTER. Cambiás el modelo.**
> LoRA, QLoRA. Entrenás pesos nuevos. Le enseñás jerga, formato, estilo, una tarea de clasificación. Requiere datos etiquetados y una GPU. Vive en la GPU — **no en el celular**.
>
> **Eje 2: la SKILL. Cambiás las herramientas.**
> Un archivo de texto plano, `SKILL.md`. Le das capacidades: buscar algo, consultar una base, dibujar un gráfico, llamar a otro modelo. **Cero entrenamiento. Cero GPU.** Corre en el celular, offline.
>
> Son cosas distintas y se combinan. Un modelo fine-tuneado en jerga periodontal (adapter) **más** una skill que consulta la historia clínica (skill) es un sistema. Un modelo fine-tuneado sin herramientas es un loro entrenado. Una skill sobre un modelo genérico es una herramienta sin criterio.
>
> Si se llevan un solo concepto de las dos horas, que sea este."

---

### SLIDE 13 — Function calling nativo (DEMO EN VIVO)
**⏱ 0:08 · 22 min** ← *el bloque más largo del taller*

**🎙 Qué decir (5 min de setup)**

> "Gemma 4 tiene **function calling nativo, implementado con seis tokens especiales dedicados**. No es prompt engineering. No es un parche post-training. El modelo fue entrenado sabiendo cuándo está adentro de una llamada a herramienta y cuándo no.
>
> Cuatro cosas:
>
> **Uno: el formato SKILL.md es abierto.** Es el estándar de `agentskills.io` — el mismo que usa Claude. **No es un archivo propietario de Google.** Eso importa: lo que aprendan hoy se traslada.
>
> **Dos: el modelo decide.** Qué herramienta invocar, en qué orden, y cómo componer la respuesta. Autónomo.
>
> **Tres: todo on-device.** Cuatro mil tokens a través de dos skills, en menos de tres segundos, en un teléfono.
>
> **Cuatro:** esto resuelve el *prompt bloat*. Dejás de meter cuatro mil palabras en el system prompt y cargás solo la capacidad que necesitás, cuando la necesitás."

**🎙 DEMO (17 min) — escribir la skill EN VIVO**

Abrí un editor. Escribí `SKILL.md` desde cero, frente a ellos. Narrá cada bloque.

> "Vamos a hacer una skill que agarre la **foto de una etiqueta de un frasco de laboratorio** y devuelva JSON estructurado. Bioingeniería pura: es el problema de entrada de datos de cualquier laboratorio del país.
>
> El frontmatter: `name`, `description`. La `description` es lo más importante del archivo — **es lo que el modelo lee para decidir si esta skill aplica**. Si la descripción es vaga, la skill nunca se activa.
>
> Ahora las instrucciones. Fíjense que le escribo al modelo, no al usuario…
>
> Ahora el esquema de salida. Le doy un ejemplo, no una especificación abstracta. Los modelos chicos imitan mejor de lo que obedecen.
>
> Ahora los casos borde: qué hace si el campo no está, qué hace si no puede leer. **Nunca inventar.** `null` explícito."

→ Importar la skill al Gallery (URL o archivo local).
→ Sacar una foto de una etiqueta real, ahí mismo.
→ Mostrar el JSON.

> "Trece minutos. En el celular. Sin internet. Sin entrenar nada."

**📎 Fuente**
- Function calling nativo en las cuatro variantes, con tokens especiales dedicados — no es un parche post-training.
- Agent Skills en Google AI Edge Gallery: workflows agénticos multi-paso y autónomos enteramente on-device, con Gemma 4. Casos de uso: aumentar la base de conocimiento, producir contenido interactivo (resúmenes, flashcards, visualizaciones), y expandir capacidades integrando otros modelos (TTS, generación de imágenes).
- El formato es SKILL.md, de agentskills.io — no un archivo propietario de Google.
- LiteRT-LM procesa ~4.000 tokens a través de dos Agent Skills en < 3 s. El modelo decide autónomamente qué herramientas invocar y en qué secuencia.
- Repositorio oficial: `github.com/google-gemma/gemma-skills` (skills `gemma-dev` y `gemma-trainer`). Instalación: `npx skills add google-gemma/gemma-skills --skill gemma-dev`.

**⚠ Riesgo:** escribir código en vivo delante de 80 personas sale mal si no lo ensayaste **tres veces**. Ensayalo tres veces. Tené la versión final en un gist como red de contención.

---

### SLIDE 14 — El gotcha del runtime
**⏱ 0:30 · 5 min**

**🎙 Qué decir**

> "Ahora la parte que les va a costar tres horas si no se las digo.
>
> **La capacidad es del modelo. El soporte es del runtime.**
>
> Con **vLLM**: si no habilitás thinking en el chat template, **el agente simplemente no llama herramientas**. Y no vas a entender por qué, porque el modelo responde normal, solo que ignora las tools. El flag es `chat_template_kwargs` con `enable_thinking: true`. Y ojo: **ese mismo flag prende razonamiento Y function calling al mismo tiempo**. Están acoplados.
>
> Con **Docker Model Runner**: hay reportes de que hace falta el shim `GemmaFunctionCallingMixin` del ADK, que convierte las declaraciones de tools en prompts de texto.
>
> ¿Ven la contradicción? La documentación oficial dice 'function calling nativo'. La realidad del runtime dice 'depende'. **Las dos cosas son ciertas.** La capacidad está en los pesos; el soporte está en el software que los ejecuta, y ese software va más atrás.
>
> Lección general, y esta les va a servir toda la carrera: **cuando algo no anda, chequeen el runtime antes de culpar al modelo.**"

**📎 Fuente**
- Guillaume Laforge (ADK Java + Gemma 4): "For function calling (tool use) to work correctly with Gemma 4 on vLLM... you must enable the thinking capability in the chat template. This is done via the chat_template_kwargs / enable_thinking parameter, which enables thinking but also function calling at the same time."
- Blog de Google Cloud Community (ADK + Gemma 4 + Docker Model Runner): reportan la necesidad del `GemmaFunctionCallingMixin` de ADK para convertir declaraciones de tools en prompts de texto en ese runtime específico.
- La documentación de Google Cloud confirma soporte explícito de structured tool use, JSON output, planificación multi-paso y thinking mode configurable. ADK lista Gemma 4 como modelo soportado.

---

### SLIDE 15 — Tamaño para agentes
**⏱ 0:35 · 4 min**

**🎙 Qué decir**

> "Contraintuitivo, y les va a ahorrar el fin de semana.
>
> **El modelo más grande no es el mejor agente.**
>
> Un agente hace muchos viajes de ida y vuelta: piensa, llama una tool, lee el resultado, piensa de nuevo, llama otra. La latencia **se multiplica por cada roundtrip**.
>
> - **E2B**: máxima velocidad. Solo si la tarea es simple.
> - **E4B**: el sweet spot. Alrededor de 22 segundos para consultas simples; unos dos minutos y medio para las complejas que necesitan autocorrección de SQL.
> - **12B**: si necesitás imagen o audio dentro del loop.
> - **26B y 31B**: **demasiado lentos para loops multi-roundtrip.** Sirven para una sola pasada, no para un agente.
>
> El viernes a la noche alguien va a querer usar el 31B 'porque es mejor'. No lo es. Para esto, no."

**📎 Fuente**
- Google Cloud Community, "Run AI Agents Locally with Google ADK, Gemma 4 & Docker": "Pick the right Gemma 4 variant for local agents — 26B / 31B are too slow for multi-roundtrip loops. E4B (the latest default) is the sweet spot: ~22s for simple queries, ~2.5 min for complex ones requiring SQL self-correction. Drop to E2B only if you need maximum speed."

---

### SLIDE 16 — LoRA en noventa segundos
**⏱ 0:39 · 4 min**

**🎙 Qué decir**

> "Cambio de eje. Adapters.
>
> LoRA en una fórmula:
>
> **y = x·W + x·A·B**
>
> `W` es el modelo base. **Congelado. Nunca se toca.**
> `A·B` es el adapter: dos matrices de rango bajo que se entrenan.
>
> Los números:
> - Entrenás entre el **0,2% y el 1%** de los parámetros.
> - Un adapter a rango 16 pesa **entre 30 y 100 MB**.
> - El overhead de cómputo es **menos del 1% por capa** a rango 16. Menos del 7% incluso a rango 64.
>
> QLoRA es lo mismo, pero el base se carga en 4 bits (NF4). Aproximadamente el 90% de la calidad de LoRA, en la mitad de la memoria.
>
> Y ahora quiero que se queden con **una sola frase** de esta slide, porque es el pivote de todo lo que viene:
>
> **El base nunca se toca. Por eso podés tener muchos adapters sobre un mismo base.**"

**📎 Fuente**
- Cálculo de overhead: para una proyección Q de 4096×4096 con rango 16, la base hace ~16,7M multiply-adds y el LoRA agrega ~130K → 0,78% de overhead. A r=64 sigue bajo 7%.
- QLoRA: 4-bit NF4 en el base, adapters en 16-bit; ~90%+ de la calidad de LoRA en GPUs mucho más chicas.
- LoRA/QLoRA actualizan 0,2–1% de los parámetros.

---

### SLIDE 17 — VRAM real (gráfico)
**⏱ 0:43 · 4 min**

**🎙 Qué decir**

> "Números reales. Y quiero ser explícito con la fuente: **esto sale de la documentación de Unsloth, no de un blog de SEO**. Hay mucha basura escrita sobre Gemma 4; esta es la fuente autoritativa.
>
> - E2B entrena en **8 GB**.
> - E4B necesita **10 GB**.
> - Se puede hacer **reinforcement learning en 9 GB**.
> - E4B con LoRA: **17 GB**.
> - 31B con QLoRA: **22 GB**.
> - El MoE 26B-A4B con LoRA: más de **40 GB** — ese sí se les escapa.
>
> Traducción: la **T4 gratis de Colab, de 16 GB, alcanza para fine-tunear E4B en QLoRA**. Una RTX 3060 de 12 GB alcanza para E2B y E4B.
>
> Y una recomendación explícita de Unsloth que va contra la intuición: **es mejor entrenar E4B en QLoRA que E2B en LoRA**. El E4B es más grande y la pérdida por cuantizar es despreciable.
>
> Además Unsloth entrena aproximadamente **1,5 veces más rápido con ~60% menos VRAM** que un setup con Flash Attention 2, sin pérdida de precisión.
>
> Conclusión: **'no tengo GPU' dejó de ser una excusa válida.** Ahora la excusa tiene que ser sobre los datos. Y esa sí me la creo."

**📎 Fuente**
- Documentación de Unsloth (`unsloth.ai/docs/models/gemma-4/train`): "Gemma 4 E2B trains on 8GB VRAM. E4B requires 10GB VRAM." / "You can also train Gemma 4 with reinforcement learning (RL) on 9GB VRAM. Gemma 4 E2B LoRA works on 8-10GB VRAM. E4B LoRA requires 17GB VRAM. 31B QLoRA works with 22GB and 26B-A4B LoRA needs >40GB." / "Unsloth trains Gemma 4 ~1.5x faster with ~60% less VRAM than FA2 setups (no accuracy loss)." / "It is recommended to train E4B QLoRA rather than E2B LoRA as the E4B is bigger and the quantization accuracy difference is miniscule."

---

### SLIDE 18 — Las cuatro trampas
**⏱ 0:47 · 5 min** ← *esta slide sola justifica que hayan venido*

**🎙 Qué decir**

> "Cuatro errores. Los van a cometer a las tres de la mañana del sábado. Se los adelanto ahora.
>
> **Uno: el MoE se lleva mal con 4 bits.** El routing del 26B-A4B y la cuantización a 4-bit **interactúan pésimo**. Unsloth recomienda explícitamente LoRA en 16-bit para el MoE, no QLoRA. Si lo cuantizan a 4 bits, el modelo va a andar mal y no van a saber por qué.
>
> **Dos: el rol se llama `model`, no `assistant`.** Gemma 4 usa `model` como rol del asistente en los mensajes. Si arman el dataset con `assistant`, **entrena mal y no se enteran hasta la evaluación**. Silencioso y letal.
>
> **Tres: perdiste el razonamiento.** Si el fine-tune mató el thinking mode, es porque no mezclaron ejemplos de razonamiento. Unsloth recomienda mantener **al menos 75% de ejemplos con reasoning** si les importa preservar esa capacidad. Y para conversaciones multi-turno: en el target de entrenamiento va **solo la respuesta final visible**, no los bloques de pensamiento previos.
>
> **Cuatro: anda en Colab, se rompe en Ollama.** La causa número uno es **chat template mismatch**: el runtime de inferencia usa un template distinto del que usaron para entrenar. Verifiquen el template al exportar.
>
> **Bonus, y este es gratis:** si ven un **loss de 13 a 15** en E2B o E4B, **es normal**. Es un quirk conocido de los modelos multimodales. No lo arreglen. No rompan nada tratando de arreglarlo."

**📎 Fuente**
- Unsloth / guías derivadas: "Because the 26B-A4B is a Mixture-of-Experts model, Unsloth recommends 16-bit LoRA instead of 4-bit QLoRA. The MoE routing and 4-bit quantization interact poorly."
- "Role naming: Gemma 4 uses `model` instead of `assistant` as the assistant role in messages."
- "Unsloth recommends keeping at least 75% reasoning examples if you care about that capability. For multi-turn conversations, only include the final visible answer in the training target."
- "Chat template mismatch after export... This is the most common cause of degraded post-export behavior."
- Unsloth docs: "If you see Gemma-4 E2B and E4B having a loss of 13-15, this is perfectly normal — this is a common quirk of multimodal models."
- Hiperparámetros de arranque razonables: `r=16`, `lora_alpha=16`, `lora_dropout=0`, target modules `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj`. Regla: `alpha = rank` mantiene el learning rate efectivo; `alpha = 2*rank` hace el adapter más fuerte. Subir a rango 32 o 64 si el dominio está lejos del pretraining.

---

### SLIDE 19 — Fine-tuning o RAG
**⏱ 0:52 · 4 min**

**🎙 Qué decir**

> "La pregunta que hay que hacerse **antes** de encender la GPU.
>
> **Fine-tuneá cuando necesitás:**
> - Formato de salida consistente. JSON, FHIR, un informe estructurado.
> - Jerga de dominio. CIE-10, terminología periodontal, nomenclatura de laboratorio.
> - Clasificación sobre sus propias imágenes.
> - Menos latencia — el prompt se acorta porque el modelo ya sabe el contexto.
>
> **NO fine-tunees para:**
> - Meterle conocimiento nuevo. Para eso, **RAG**. El fine-tuning enseña **patrones**, no hechos.
> - Datos que cambian todas las semanas.
> - Arreglar algo que un buen prompt ya resuelve. **Prueben prompting primero. En serio.**
> - Impresionarme a mí. No me impresiona.
>
> Tamaños de dataset realistas: **200 a 1.000 ejemplos** para transferencia de estilo. **500 a 5.000** para clasificación.
>
> Y la regla de oro del hackathon: **80% pipeline de datos y evaluación, 20% modelo.** El equipo que se pone a entrenar desde cero pierde. Siempre."

**📎 Fuente**
- Guías de fine-tuning de Gemma 4: "Use it for domain jargon, strict formats, or brand tone — not general knowledge." / "Data size: Style transfer needs 200-1,000 samples; classification needs 500-5,000 samples."
- "Fine-tuning makes sense when you need the model to learn patterns, not just look up facts."
- Fine-tuning da: formato consistente, conocimiento de dominio, y menor latencia (prompts más cortos porque el modelo ya conoce el contexto).

---

### SLIDE 20 — El resultado (gráfico 33% → 89%)
**⏱ 0:56 · 4 min**

**🎙 Qué decir**

> "Un resultado médico, reproducible, en una sola época.
>
> **MedGemma 4B fine-tuneado sobre un dataset de MRI cerebral para clasificar cáncer: de 33% a 89% de accuracy. Una sola época. LoRA. Dataset chico.**
>
> Eso, señores, **es un proyecto de hackathon terminado.** Cincuenta y seis puntos de accuracy.
>
> Ahora la honestidad, porque si no se las digo yo se las va a decir la realidad: el notebook oficial de MedGemma con GRPO — que es reinforcement learning — va de **14,1% a 70,5%**. Impresionante. Pero pide una **GPU de 40 GB y unas once horas en una A100**. Eso **no es material de fin de semana**. No lo intenten el sábado.
>
> LoRA sí. RL no. Elijan bien dónde gastan las 48 horas."

**📎 Fuente**
- Tutorial de fine-tuning de MedGemma sobre MRI cerebral (DataCamp): "The accuracy jumped from 33% to 89% with only 1 epoch. Fine-tuned metrics: {'accuracy': 0.8927, 'f1': 0.8926}"
- Notebook oficial de MedGemma con GRPO: "The RL-tuning with GRPO improved the model's accuracy from a baseline of 14.1% to 70.5%." / "This guide requires a GPU that supports bfloat16 data type and has at least 40 GB of memory." / "~11 hrs for 1700 training steps on an A100 40GB GPU."
- Configuración del pipeline oficial de Google Health para histopatología: `r=16, lora_alpha=16, lora_dropout=0.05, target_modules="all-linear"`, con **patient-level splitting para evitar data leakage** — decilo, es la clase de detalle que separa un proyecto serio de una demo.

**💡 Punto crítico que agregar acá (no está en la slide, dilo):**

> "Un detalle de ese pipeline oficial que quiero que se lleven: hacen **split a nivel de paciente**, no a nivel de imagen. ¿Por qué? Porque si dos cortes del mismo paciente caen uno en train y otro en test, tu accuracy está inflada y **no lo sabés**. Ese es el error número uno de los proyectos de ML médico de estudiantes. Y lo voy a buscar cuando los juzgue."

---

### SLIDE 21 — Honestidad epistémica
**⏱ 1:00 · 3 min**

**🎙 Qué decir**

> "Van a leer en cinco blogs distintos la frase: *'un E4B fine-tuneado iguala a un 31B prompteado'*.
>
> **No está en ningún benchmark revisado.** Está en blogs. Puede ser cierta. Yo creo que probablemente sea cierta para muchas tareas. Pero no la puedo probar, y ustedes tampoco.
>
> **Díganla como hipótesis de trabajo, no como hecho.** Sobre todo si la ponen en un slide frente a un jurado.
>
> ¿Qué SÍ es defendible? **LoRA Land**: 310 modelos fine-tuneados. **301 de 310 superaron a su modelo base. 224 de 310 superaron a GPT-4 en su tarea específica.**
>
> Eso es un paper con datos. Y dice algo más fuerte y más útil: **un modelo chico y especializado le gana a un modelo gigante generalista — en esa tarea, y solo en esa tarea.**
>
> La diferencia entre las dos frases es la diferencia entre un ingeniero y un influencer. Elijan."

**📎 Fuente**
- LoRA Land (arXiv 2405.00732): "After fine-tuning, 301/310 models surpass their base model counterpart, while 224/310 fine-tuned LLMs surpass the benchmark set by GPT-4." Mejoras de +26,3 a +51,2 puntos según el modelo base, +38,7 en promedio.
- La afirmación "un E4B fine-tuneado (4,5B) puede igualar a un 31B prompteado en tu tarea" **aparece en blogs de vendors, no en benchmarks revisados**. Tratarla como hipótesis.

---

### SLIDE 22 — LA SÍNTESIS: multi-LoRA
**⏱ 1:03 · 7 min** ← **EL CLÍMAX DE LAS DOS CHARLAS**

**🎙 Qué decir** *(bajá el ritmo, esto es lo que se van a llevar)*

> "Bueno. Acá se juntan los dos ejes.
>
> Se acuerdan: el base nunca se toca. Un adapter pesa 60 megas.
>
> Entonces… **¿por qué tendría un solo modelo?**
>
> Miren el diagrama.
>
> **Un solo Gemma 4 E4B, cargado UNA vez en la GPU.** Cuatro gigas.
>
> Encima: cuatro adapters. Uno entrenado para **extracción de datos de informes de laboratorio**. Otro para **notas periodontales**. Otro para **preguntas sobre FHIR**. Otro para **dictado clínico**. Sesenta megas cada uno.
>
> Y un **router**: el agente elige qué adapter usar, **por request**.
>
> Esto no es un truco de pizarrón. **vLLM lo hace en producción hoy**, con el flag `--lora-modules`.
>
> Lo que están viendo es **un sistema multi-agente entero, con cuatro especialistas médicos, corriendo en una sola placa de video de estudiante.**
>
> Y les voy a decir algo más: **esto es exactamente lo que estoy construyendo en Histora.** No es un ejemplo de juguete. Es la arquitectura de un producto real que tiene que cumplir HIPAA.
>
> **Ustedes lo pueden construir este fin de semana.**"

**📎 Fuente**
- vLLM intercambia adapters **por request con overhead sub-milisegundo** usando su LoRAManager.
- Carga on-demand desde disco o almacenamiento compatible con S3 vía `--lora-modules`; los adapters se cargan al primer request y se desalojan de un caché LRU.
- Un adapter a rango 16 pesa ~30–100 MB según el tamaño del base.
- Reporte de performance: hasta **200 adapters concurrentes en una sola A100 con menos de 5% de overhead de latencia** comparado con un deployment de un solo modelo.
- Todos los adapters deben compartir la misma arquitectura base y el mismo dtype.

---

### SLIDE 23 — Los números del multi-LoRA
**⏱ 1:10 · 4 min**

**🎙 Qué decir**

> "Los cuatro números que hacen que esto sea viable y no una fantasía:
>
> - **Sub-milisegundo** de overhead al intercambiar adapter por request.
> - **Alrededor de 200 adapters concurrentes** en una sola A100, con menos de 5% de latencia extra.
> - **Menos del 1%** de cómputo extra por capa a rango 16.
> - **Carga LRU on-demand** desde disco o S3: no tenés que tener todo en memoria.
>
> Y ahora **las dos restricciones**, que hay que decir en voz alta porque si no alguien se va a estrellar:
>
> **Uno:** todos los adapters comparten **arquitectura base y dtype**. No podés mezclar un adapter de E4B con uno de 12B sobre el mismo servidor.
>
> **Dos**, y esto cierra el círculo de toda la charla: **esto es serving en GPU. NO aplica al Gallery en el celular.** En el borde, el mecanismo de especialización **no es el adapter — es la skill.**
>
> ¿Ven? Vuelve la slide de los dos ejes. **Adapter en la GPU. Skill en el borde.** Ese es el mapa completo."

---

### SLIDE 24 — MedGemma: el catálogo de proyectos
**⏱ 1:14 · 5 min**

**🎙 Qué decir**

> "Ahora les doy el menú. **Cada viñeta de esta slide es un proyecto entero.**
>
> - **Imagen 3D**: MedGemma 1.5 interpreta **volúmenes completos de CT y MRI**, no rebanada por rebanada. Es el **primer modelo abierto** que hace eso.
> - **Histopatología WSI**: múltiples parches de un whole-slide interpretados en simultáneo. **+47% de macro F1** sobre la versión anterior.
> - **Localización anatómica**: bounding boxes sobre radiografía de tórax. El IoU pasó de **3% a 38%**.
> - **Longitudinal**: radiografía de tórax comparada contra estudios previos del mismo paciente.
> - **Documentos y EHR**: extracción estructurada de informes de laboratorio. **EHRQA de 68% a 90%** — ese es el salto más grande de todos.
> - **MedASR**: dictado clínico. **58% menos errores que Whisper large-v3** en dictado de tórax. Word error rate de 12,5% a 5,2%.
>
> Y un consejo de arquitectura que vale plata: **si tu tarea es clasificar sin generar texto, no uses MedGemma. Usá MedSigLIP**, que es el encoder solo. Es más chico, más rápido y más preciso para eso. Lo dice la propia documentación."

**📎 Fuente**
- Blog de Google Research: MedGemma 1.5 4B habilita imagen de alta dimensión (CT, MRI, histopatología), imagen longitudinal (series temporales de Rx de tórax), localización anatómica, y comprensión de documentos médicos.
- Technical Report (arXiv 2604.05081): +11% en clasificación de condiciones en MRI 3D, +3% en CT 3D, **+47% macro F1 en whole-slide pathology**, **+35% de IoU en localización anatómica** en Rx de tórax, +4% de macro accuracy en análisis longitudinal, **+5% MedQA**, **+22% EHRQA**.
- Métricas absolutas: CT de 58% → 61%; MRI de 51% → 65%; Chest ImaGenome IoU de 3% → 38%; MS-CXR-T macro accuracy de 61% → 66%; extracción de informes de laboratorio macro F1 de 60% → 78%; MedQA de 64% → 69%; EHRQA de 68% → 90%.
- MedASR: WER en dictado de Rx de tórax de 12,5% → 5,2% (58% menos errores); en un benchmark interno de dictado médico diverso, de 28,2% → 5,2% (82% menos errores).
- Documentación oficial: "For medical image-based applications that do not involve text generation, such as data-efficient classification, zero-shot classification, or content-based or semantic image retrieval, the MedSigLIP image encoder is recommended."

---

### SLIDE 25 — La letra chica
**⏱ 1:19 · 4 min**

**🎙 Qué decir**

> "**Lean la licencia. Sí, ustedes.** Y sobre todo los que quieran comercializar algo después.
>
> **Gemma 4 es Apache 2.0.** Comercialmente permisiva. Hacé lo que quieras. Es un cambio grande respecto de los 'Gemma Terms of Use' anteriores, que tenían restricciones de uso aceptable, se extendían de forma ambigua a modelos entrenados con datos sintéticos generados por Gemma, y podían actualizarse unilateralmente. Muchos equipos legales corporativos se negaban a usarlos por eso.
>
> **MedGemma 1.5 NO es Apache 2.0.** Se rige por los *Health AI Developer Foundations terms of use*. Es otra cosa. **Léanla antes de armar una empresa arriba.**
>
> Y además: **MedGemma 1.5 sigue construido sobre Gemma 3**, no sobre Gemma 4. Es un modelo de 4B multimodal, instruction-tuned.
>
> Lo cual me lleva al punto más importante de esta slide:
>
> **Nadie fine-tuneó Gemma 4 al dominio médico todavía.**
>
> Ese hueco está abierto. **Eso no es un ejercicio de hackathon. Eso es una tesis.** Y si a alguno le interesa, hablemos."

**📎 Fuente**
- Model card de MedGemma: "MedGemma is a collection of Gemma 3 variants that are trained for performance on medical text and image comprehension." / "License: The use of MedGemma is governed by the Health AI Developer Foundations terms of use."
- MedGemma 1.5 está disponible **solo como variante 4B multimodal instruction-tuned**.
- Gemma 4 bajo licencia Apache 2.0, comercialmente permisiva. Las licencias previas de Gemma tenían restricciones de uso aceptable y podían actualizarse unilateralmente.

---

### SLIDE 26 — Cómo los voy a juzgar
**⏱ 1:23 · 4 min**

**🎙 Qué decir**

> "Soy jurado del hackathon. Esto no es un secreto, así que se los doy ahora. Suban el nivel de todos los proyectos, incluido el de ustedes.
>
> **30% — ¿Midieron algo?** Quiero un baseline y un número después. **Sin evaluación no hay proyecto, hay demo.** Y una demo es entretenimiento.
>
> **25% — ¿El dato está protegido?** Si el PHI salió a una API de terceros, el proyecto está **muerto por diseño**. No importa lo bien que funcione.
>
> **25% — ¿Corre?** En vivo, en tu máquina, delante mío. **No un video. No un slide.**
>
> **20% — ¿Saben dónde falla?** Si me venís a decir que funciona siempre, **no lo probaste**. Mostrame el caso que rompe. El equipo que me muestra su propio fallo gana puntos, no los pierde.
>
> Y lo que **NO** puntúo: el tamaño del modelo, la cantidad de features, y lo lindo que quedó el frontend."

---

### SLIDE 27 — Regulatorio
**⏱ 1:27 · 4 min**

**🎙 Qué decir**

> "Antes de que alguien se entusiasme demasiado.
>
> **Uno: nada de esto es un dispositivo médico.** Ni MedGemma, ni Gemma 4, ni lo que construyan este fin de semana. La documentación oficial de DeepMind lo dice literalmente: las salidas de estos modelos **no están destinadas a informar diagnóstico clínico, decisiones de manejo del paciente, ni recomendaciones de tratamiento**.
>
> **Dos: el EU AI Act clasifica la IA médica como sistema de alto riesgo.** Validación clínica obligatoria antes de producción. MDR e IVDR aplican.
>
> **Tres: la responsabilidad es del que despliega, no del que entrenó el modelo.** Si vos lo ponés en una clínica, **es tuyo**. Google no te va a defender.
>
> **Cuatro: anonimizá antes de tocar nada.** Y si van a usar cloud, elijan la región. En serio. Esto es literalmente lo que hago todos los días.
>
> Esto no es burocracia. **Es la diferencia entre un proyecto que puede existir y uno que no.**"

**📎 Fuente**
- DeepMind, página de MedGemma: "MedGemma is not intended to be used without appropriate validation, adaptation and/or making meaningful modification by developers for their specific use case. The outputs generated by these models are not intended to directly inform clinical diagnosis, patient management decisions, treatment recommendations, or any other direct clinical practice applications."
- Consultoras especializadas en integración de MedGemma en la UE: MDR/IVDR aplican; el EU AI Act clasifica la IA médica como sistema de alto riesgo; la responsabilidad recae en el usuario, no en el desarrollador del modelo; GDPR Art. 9 (categorías especiales); recomendación explícita de **self-hosting** para datos de pacientes y anonimización obligatoria antes de cualquier procesamiento.

---

### SLIDE 28 — Recursos
**⏱ 1:31 · 3 min**

**🎙 Qué decir**

> "Todo en una slide. Sáquenle foto.
>
> Y una última cosa: **MedGemma Impact Challenge en Kaggle. Cien mil dólares en premios.**
>
> Lo que construyan este fin de semana **no tiene por qué morir el domingo a la noche.** Ese es el punto. Un hackathon es una excusa para empezar algo, no para terminarlo."

**📎 Fuente**
- Google Research anunció el MedGemma Impact Challenge, un hackathon en Kaggle con **US$ 100.000 en premios**, junto con el lanzamiento de MedGemma 1.5.
- También existe el **Gemma 4 Good Challenge** en Kaggle, para construir productos con impacto positivo.

---

### SLIDE 29 — Cierre
**⏱ 1:34 · 1 min + preguntas**

**🎙 Qué decir**

> "El modelo es lo fácil.
>
> **Los datos, la evaluación y la regulación son el trabajo.**
>
> Todo lo que les mostré hoy — los cinco tamaños, los adapters, las skills, el multi-LoRA — es la parte que ya está resuelta. Está en un repo. Es gratis. Se descarga en veinte minutos.
>
> Lo que no está resuelto es lo que ustedes van a tener que hacer: conseguir los datos, etiquetarlos bien, medir de verdad, y no violar la ley.
>
> Ahora vayan y rompan algo.
>
> Nos vemos en el hackathon."

---
---

## Anexo A — Preguntas que te van a hacer (y las respuestas)

**"¿Por qué no uso GPT-4 / Claude / Gemini y listo?"**
> Porque el dato de salud no puede salir. Punto. Si tu caso de uso no toca datos de pacientes, usá lo que quieras — probablemente sea mejor. En cuanto toca PHI, la conversación cambia de 'cuál es mejor' a 'cuál es legal'.

**"¿Cuánto tarda en entrenar?"**
> Depende del dataset. Con 1.000 ejemplos y QLoRA sobre E4B en una T4 de Colab, del orden de una hora. El notebook oficial de MedGemma con RL tarda 11 horas en una A100 — eso te da la escala del otro extremo.

**"¿Se puede fine-tunear el 12B multimodal?"**
> Unsloth soporta fine-tuning de visión, texto, audio y RL para Gemma 4, incluyendo el 12B. La VRAM sube. Verificá los números actuales en su doc antes de comprometerte.

**"¿Y si mis datos son pocos?"**
> Entonces probablemente no necesites fine-tuning: necesitás prompting bueno + RAG. El fine-tuning con 50 ejemplos no te va a dar nada bueno, te va a dar overfitting con cara de éxito.

**"¿El modelo puede diagnosticar?"**
> No. Y decir que sí es, además de falso, potencialmente ilegal. Puede asistir, estructurar, priorizar, transcribir. No diagnostica.

**"¿Cuál es la trampa de todo esto?"**
> La evaluación. Es fácil hacer que un modelo genere algo que parece bien. Es difícil demostrar que está bien. Y en medicina, "parece bien" no alcanza.

---

## Anexo B — Errores que voy a estar buscando como jurado

1. **Data leakage a nivel de paciente.** Cortes del mismo paciente en train y test. El pipeline oficial de MedGemma hace patient-level splitting por esto. Si tu accuracy es sospechosamente alta, es esto.
2. **Sin baseline.** Un número solo no es un resultado.
3. **PHI en una API de terceros.** Muerte instantánea.
4. **Métrica equivocada.** Accuracy en un dataset desbalanceado no dice nada. Quiero F1, o AUC, o sensibilidad/especificidad, según el caso.
5. **Demo grabada.** Si no corre en vivo, no corre.
6. **Chat template mismatch** que hace que el modelo funcione en el notebook y no en la app. Clásico.
7. **Confundir "el modelo dijo X" con "X es verdad".**
