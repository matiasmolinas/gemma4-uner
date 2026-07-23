"""
Gemma 4 multimodal en tu laptop, con Ollama.

Gemma 4 12B es encoder-free — imagen y audio entran directo al backbone del LLM.
Este script muestra las tres modalidades sobre el MISMO modelo, sin pipeline
de ASR separado, sin encoder de visión separado, sin internet.

Preparación:
    ollama pull gemma4:12b        # verificá el tag con `ollama list`
    pip install ollama
    # assets/radiografia.jpg y assets/dictado.wav ya vienen en el repo;
    # reemplazalos por tu propio material (anonimizado) cuando armes tu proyecto

Uso:
    python demo_multimodal.py texto
    python demo_multimodal.py imagen
    python demo_multimodal.py audio

NOTA: el soporte de audio depende de la versión del runtime de Ollama
(verificado jul-2026: aún no funciona — descarta el campo en silencio).
El camino verificado para audio es LiteRT-LM CLI: ver README.
"""

import sys
from pathlib import Path

import ollama

MODELO = "gemma4:12b"
ASSETS = Path(__file__).parent / "assets"


def texto():
    """Baseline. Sin imagen, sin audio. Para calibrar la latencia del proyector."""
    r = ollama.chat(
        model=MODELO,
        messages=[
            {
                "role": "user",
                "content": (
                    "Explicá en 3 oraciones por qué un modelo que corre on-device "
                    "es preferible a una API en la nube cuando se procesan datos "
                    "de salud. No uses viñetas."
                ),
            }
        ],
    )
    print(r["message"]["content"])


def imagen():
    """Visión: sin encoder. Una proyección lineal y adentro."""
    img = ASSETS / "radiografia.jpg"
    if not img.exists():
        sys.exit(f"Falta {img}. Poné una imagen ahí.")

    r = ollama.chat(
        model=MODELO,
        messages=[
            {
                "role": "user",
                "content": (
                    "Describí esta imagen médica de forma estructurada. Devolvé JSON con: "
                    "modalidad, region_anatomica, orientacion, calidad_tecnica, "
                    "hallazgos_visibles (array), limitaciones (array). "
                    "IMPORTANTE: esto NO es un diagnóstico. Si algo no se ve con "
                    "claridad, decilo en limitaciones en vez de inventarlo. "
                    "Respondé solo el JSON."
                ),
                "images": [str(img)],
            }
        ],
    )
    print(r["message"]["content"])


def audio():
    """Audio nativo: la señal cruda se proyecta al mismo espacio que los tokens."""
    wav = ASSETS / "dictado.wav"
    if not wav.exists():
        sys.exit(f"Falta {wav}. Grabá 15 s de dictado clínico.")

    r = ollama.chat(
        model=MODELO,
        messages=[
            {
                "role": "user",
                "content": (
                    "Escuchá este dictado clínico y devolvé JSON con: "
                    "transcripcion_literal, motivo_consulta, hallazgos (array), "
                    "plan (array), terminos_dudosos (array de palabras que no "
                    "entendiste con seguridad). No inventes nada que no se haya dicho."
                ),
                # El campo puede llamarse 'audios' o ir dentro de 'images' según
                # la versión del runtime. Si esto falla, ver README -> LiteRT-LM.
                "audios": [str(wav)],
            }
        ],
    )
    print(r["message"]["content"])


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "texto"
    {"texto": texto, "imagen": imagen, "audio": audio}.get(modo, texto)()
