from openai import OpenAI
from .prompts import PROMPTS

client = OpenAI()


def responder(texto):

    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "Eres el asistente del Dr. Carlos Giraldo. Responde breve y claro."
            },
            {
                "role": "user",
                "content": texto
            }
        ],
        max_tokens=120
    )

    return completion.choices[0].message.content


def responder_intent(intent):

    prompt = PROMPTS.get(intent)

    if not prompt:
        return "¿En qué puedo ayudarte?"

    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": prompt
            }
        ],
        max_tokens=120
    )

    return completion.choices[0].message.content