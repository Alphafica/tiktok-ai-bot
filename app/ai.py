from openai import OpenAI
from .config import OPENAI_API_KEY
from .prompts import SYSTEM_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)


def responder(mensaje):

    try:

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": mensaje}
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:

        print("Error IA:", e)

        return "En este momento estamos teniendo un problema técnico. Escríbenos por WhatsApp y te ayudamos."