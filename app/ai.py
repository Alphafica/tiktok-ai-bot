from openai import OpenAI
from .config import OPENAI_API_KEY
from .prompts import PROMPTS

client = OpenAI(api_key=OPENAI_API_KEY)


def responder_inteligente(intent):

    prompt = PROMPTS.get(intent)

    if not prompt:
        return "¿En qué puedo ayudarte?"

    respuesta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Eres el asistente del Dr. Giraldo especialista en pérdida de peso."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return respuesta.choices[0].message.content