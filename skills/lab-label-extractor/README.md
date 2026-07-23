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

## Probarla desde la terminal (LiteRT-LM CLI)

El mismo flujo foto → JSON, sin celular ni browser. LiteRT-LM es el runtime del
Gallery, y su CLI acepta imágenes con `--attachment`:

```bash
uv tool install --python 3.12 litert-lm   # una sola vez

litert-lm run \
  --from-huggingface-repo=litert-community/gemma-4-E2B-it-litert-lm \
  gemma-4-E2B-it.litertlm \
  --prompt="Extraé los datos de esta etiqueta de laboratorio y devolvé únicamente JSON con: producto, fabricante, numero_catalogo, lote, cantidad, fecha_vencimiento (YYYY-MM-DD), pictogramas_ghs, cas, confianza, campos_ilegibles" \
  --attachment web/etiqueta_prueba.jpg
```

**Verificado (jul-2026, MacBook M4): ~10 segundos** con el modelo ya cacheado
(la primera corrida descarga ~2.6 GB).

### El experimento que vale la pena hacer

Corré ese comando dos veces: una con el prompt corto de arriba, y otra pegando
como prompt el **contenido completo de `SKILL.md`** (reglas duras + enums +
ejemplo). Mismo modelo, misma foto — resultados distintos:

| Campo | Con la SKILL.md completa | Con el prompt corto |
|---|---|---|
| `fecha_vencimiento` ("Venc.: 11/2027") | `2027-11-30` ✅ (regla del último día del mes) | `2027-11-01` ⚠️ (inventó el día) |
| `confianza` | `"alta"` (enum de la skill) | `0.95` (formato inventado) |
| `pictogramas_ghs` | `["inflamable"]` (enum) | `"Fuego", "Exclamación (o similar...)"` |

**Las reglas duras y los enums de la SKILL.md no son decoración: son el
contrato.** Sin ellos, el modelo llena los huecos con formatos propios — y eso,
en un inventario real, es deuda que se propaga.

## Versión web

En [`web/`](web/) está la misma skill corriendo **en el browser** (Chrome +
WebGPU + MediaPipe LLM Inference, modelo local `.litertlm`): útil si querés una
demo sin celular, o como base para un frontend web on-device. Ver `web/README.md`
para el estado actual (la variante web de Gemma 4 es text-only por ahora).
