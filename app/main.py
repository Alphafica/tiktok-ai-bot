from fastapi import FastAPI
from .ai import responder, responder_intent
from .intents import detectar_intent
from .whatsapp import generar_link
from .database import engine, Base, SessionLocal
from .models import Lead

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/chat")
async def chat(data: dict):

    mensaje = data.get("text", "")
    contexto = data.get("context")

    intent = detectar_intent(mensaje)

    if contexto:
        intent = contexto

    db = SessionLocal()
    lead = Lead(mensaje=mensaje, intent=intent)
    db.add(lead)
    db.commit()
    db.close()

    if intent == "precio":

        respuesta = (
            "El tratamiento cuesta 1.500.000 COP e incluye 12 aplicaciones "
            "durante 3 meses. La consulta médica cuesta 200.000 COP."
        )

    elif intent in ["funciona", "resultado", "contraindicaciones"]:
        respuesta = responder_intent(intent)

    elif intent == "lead_caliente":

        whatsapp = generar_link()

        respuesta = (
            "Perfecto 🙌\n\n"
            "Puedes hablar directamente con el equipo médico aquí:\n\n"
            f"{whatsapp}"
        )


    else:

        respuesta = responder(mensaje)

    return {
        "reply": respuesta
    }