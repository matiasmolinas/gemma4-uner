# Agente con function calling nativo

Charla 2, slides 13–15.

## Setup

```bash
ollama pull gemma4:e4b
pip install -r requirements.txt
python agente_gemma4.py
```

## Qué demuestra

Tres herramientas. Ningún `if/else` que enrute. **El modelo decide qué llamar y en
qué orden.**

El prompt clave fuerza cuatro pasos:

> *"¿Nos queda cloruro de sodio? Si vence en menos de 90 días, pedí 2 más."*

buscar → calcular días → decidir → pedir.

Y el tercer prompt (*"¿qué es un pictograma GHS?"*) demuestra lo contrario:
**el modelo NO debería llamar ninguna herramienta.** Saber cuándo *no* usar una tool
es tan importante como saber cuándo usarla.

## Los dos gotchas que hay que decir en voz alta

**1. El rol es `model`, no `assistant`** — pero los resultados de herramienta siguen
usando el rol `tool`. Es una asimetría que confunde.

**2. En vLLM, `enable_thinking` prende razonamiento Y function calling al mismo tiempo.**
Están acoplados. Si tu agente no llama tools, chequeá esto antes de culpar al modelo:

```python
extra_body={"chat_template_kwargs": {"enable_thinking": True}}
```

Con Docker Model Runner hay reportes de que hace falta el shim
`GemmaFunctionCallingMixin` del ADK.

**Lección general: cuando algo no anda, chequeá el runtime antes de culpar al modelo.**

## Tamaño para agentes (contraintuitivo)

- **E4B**: el sweet spot. ~22 s consultas simples, ~2,5 min las complejas.
- **26B / 31B**: demasiado lentos para loops multi-roundtrip.

El viernes a la noche alguien va a querer el 31B "porque es mejor". No lo es. Para esto, no.
