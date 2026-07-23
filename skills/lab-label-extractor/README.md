# lab-label-extractor

Skill multimodal para **Google AI Edge Gallery**: convierte la foto de una
etiqueta de laboratorio en JSON estructurado, corriendo **on-device** con
Gemma 4 E2B o E4B, sin conexión.

Es el ejemplo de referencia de una skill bien escrita — usala como plantilla
para la tuya.

## Por qué esta skill es un buen ejemplo

- **Es multimodal.** Usa la capacidad de visión del modelo.
- **Resuelve un problema real.** Todo laboratorio del país tiene el problema de
  la carga manual de inventario.
- **Se ve funcionar en 5 segundos.** Foto → JSON. Sin ambigüedad sobre si anduvo.
- **Tiene casos borde reales.** Fechas ambiguas, campos ilegibles, unidades.
  Ahí vive el principio más importante: **null explícito > valor inventado.**

## Probarla en tu celular

1. Instalá Google AI Edge Gallery (Android o iOS).
2. Descargá **Gemma 4 E4B** adentro de la app (no alcanza con tenerlo en Ollama:
   el Gallery usa su propio formato).
3. Importá `SKILL.md` por URL o desde archivo local.
4. Sacale una foto a una etiqueta y escribí: *"digitalizá esta etiqueta"*.
5. Poné el teléfono en **modo avión** y repetí. Sigue funcionando: el dato
   nunca salió del dispositivo.

## Anatomía del archivo — lo que importa al escribir la tuya

| Bloque | Qué hace | Por qué importa |
|---|---|---|
| `description` (frontmatter) | Decide **si la skill se activa** | Es lo más importante del archivo. Si es vaga, la skill nunca corre. |
| Esquema de salida | Contrato con el sistema que consume | Dale un **ejemplo**, no una especificación abstracta: los modelos chicos imitan mejor de lo que obedecen. |
| Reglas duras | Comportamiento no negociable | Regla 1: nunca inventar. Un `null` explícito es un dato correcto; un valor inventado se propaga a todo el inventario. |
| Casos borde | Qué hace cuando el mundo no coopera | Acá se separa una demo de un producto. |

## Versión web

En [`web/`](web/) está la misma skill corriendo **en el browser** (Chrome +
WebGPU + MediaPipe LLM Inference, modelo local `.litertlm`): útil si querés una
demo sin celular, o como base para un frontend web on-device. Ver `web/README.md`
para el estado actual (la variante web de Gemma 4 es text-only por ahora).
