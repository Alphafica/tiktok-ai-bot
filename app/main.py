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

    mensaje = (data.get("text") or "").lower().strip()
    contexto = data.get("context")

    # prioridad al botón
    if contexto:
        intent = contexto
    else:
        intent = detectar_intent(mensaje)

    db = SessionLocal()

    lead = Lead(
        mensaje=mensaje,
        intent=intent
    )

    db.add(lead)
    db.commit()
    db.close()

    # RESPUESTAS

    if intent == "precio":
        respuesta = (
            "El tratamiento con Tirzepatide cuesta "
            "1.500.000 COP e incluye 12 aplicaciones durante 3 meses.\n\n"
            "La consulta médica obligatoria cuesta 200.000 COP."
        )

    elif intent == "resultado":
        respuesta = (
            "Con Tirzepatide los pacientes suelen perder "
            "entre 20% y 25% de su peso corporal "
            "cuando se combina con dieta y ejercicio."
        )

    elif intent == "funciona":
        respuesta = (
            "Tirzepatide actúa controlando el apetito, "
            "mejorando la insulina y ayudando a reducir grasa corporal."
        )

    elif intent == "contraindicaciones":
        respuesta = (
            "El tratamiento debe ser evaluado por el doctor.\n\n"
            "No se recomienda en embarazo, algunos problemas "
            "tiroideos o condiciones médicas específicas."
        )

    elif intent == "ubicacion":
        respuesta = (
            "Estamos ubicados en Ibagué, Colombia.\n\n"
            "También atendemos pacientes de otras ciudades."
        )

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
        "intent": intent,
        "reply": respuesta
    }