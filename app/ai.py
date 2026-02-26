from openai import OpenAI
from .config import OPENAI_API_KEY
from .prompts import SYSTEM_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)


def responder(texto):

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": texto}
        ],
        max_tokens=120
    )

    respuesta = completion.choices[0].message.content

    return respuesta