# lab-label-extractor

Skill para Google AI Edge Gallery. Corre **on-device**, con Gemma 4 E2B o E4B,
sin conexión. Convierte la foto de una etiqueta de laboratorio en JSON estructurado.

## Por qué esta skill y no otra

- **Es multimodal.** Usa la capacidad de visión, que es el punto de la charla.
- **Es bioingenieril.** Todo laboratorio del país tiene el problema de carga manual de inventario.
- **Se ve funcionar en 5 segundos.** Foto → JSON. Sin ambigüedad sobre si anduvo o no.
- **Tiene casos borde reales.** Fechas ambiguas, campos ilegibles, unidades. Sirve para
  enseñar el principio más importante: **null explícito > valor inventado.**

## Instalar en el Gallery

1. Abrí Google AI Edge Gallery (Android o iOS).
2. Descargá **Gemma 4 E4B** adentro de la app (no alcanza con tenerlo en Ollama).
3. Importá `SKILL.md` por URL o desde archivo local.
4. Sacá una foto de una etiqueta y prompteá: *"digitalizá esta etiqueta"*.

## Anatomía del archivo — lo que hay que explicar en vivo

| Bloque | Qué hace | Qué decir |
|---|---|---|
| `description` (frontmatter) | Decide **si la skill se activa** | "Es lo más importante del archivo. Si es vaga, la skill nunca corre." |
| Esquema de salida | Contrato con el sistema que consume | "Le doy un ejemplo, no una especificación abstracta. **Los modelos chicos imitan mejor de lo que obedecen.**" |
| Reglas duras | Comportamiento no negociable | "Regla 1: nunca inventes. `null` explícito es un dato correcto; un valor inventado se propaga a todo el inventario." |
| Casos borde | Qué hace cuando el mundo no coopera | "Acá se separa una demo de un producto." |

## Versión web (plan B)

En [`web/`](web/) está la misma skill corriendo **en el browser** (Chrome +
WebGPU + MediaPipe LLM Inference, modelo `-Web.litertlm` local). Para el
encuentro virtual es el plan B robusto: compartís la pestaña y no dependés del
teléfono. Ver `web/README.md`.

## Ensayo

Escribila **tres veces** antes de la charla. Cronometrala. El objetivo son 13 minutos,
incluyendo la foto y el resultado. Tené esta versión final en un gist como red de contención.
