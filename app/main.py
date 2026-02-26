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
    contexto = data.get("context")

    intent = detectar_intent(mensaje)

    db = SessionLocal()

    lead = Lead(
        mensaje=mensaje,
        intent=intent
    )

    db.add(lead)
    db.commit()
    db.close()

    # prioridad al contexto del botón
    if contexto:
        intent = contexto

    if intent == "precio":
        respuesta = (
            "El tratamiento con Tirzepatide cuesta "
            "1.500.000 COP e incluye 12 aplicaciones durante 3 meses. "
            "La consulta médica obligatoria cuesta 200.000 COP."
        )

    elif intent == "resultado":
        respuesta = (
            "Los pacientes suelen perder entre 20% y 25% de su peso "
            "cuando combinan Tirzepatide con dieta y ejercicio."
        )

    elif intent == "contraindicaciones":
        respuesta = (
            "El tratamiento debe ser evaluado por el doctor. "
            "No se recomienda en embarazo, ciertos problemas "
            "tiroideos o condiciones específicas."
        )

    elif intent == "ubicacion":
        respuesta = (
            "Estamos ubicados en Ibagué, Colombia "
            "y realizamos envíos a todo el país."
        )

    elif intent == "lead_caliente":

        respuesta = (
            "Perfecto. Podemos enviarte toda la información "
            "y ayudarte a iniciar el tratamiento."
        )

    else:
        respuesta = responder(mensaje)

    whatsapp = generar_link()

    return {
        "intent": intent,
        "reply": f"{respuesta}\n\nWhatsApp:\n{whatsapp}"
    }