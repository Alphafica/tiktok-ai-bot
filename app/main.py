from fastapi import FastAPI
from .ai import responder
from .intents import detectar_intent
from .whatsapp import generar_link
from .database import engine, Base, SessionLocal
from .models import Lead

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"status": "bot funcionando"}


@app.post("/chat")
async def chat(data: dict):

    mensaje = data.get("text", "")

    intent = detectar_intent(mensaje)

    db = SessionLocal()

    lead = Lead(
        mensaje=mensaje,
        intent=intent
    )

    db.add(lead)
    db.commit()
    db.close()

    if intent == "lead_caliente":

        respuesta = """
¡Perfecto!

Este tratamiento ha ayudado a muchos pacientes a bajar entre 20% y 25% de su peso.

El doctor primero realiza una consulta para evaluar tu caso.

¿Te gustaría que te enviemos toda la información por WhatsApp?
"""

    else:

        respuesta = responder(mensaje)

    whatsapp = generar_link()

    return {
        "intent": intent,
        "reply": f"{respuesta}\n\nWhatsApp:\n{whatsapp}"
    }