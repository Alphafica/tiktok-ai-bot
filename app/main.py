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

    # RESPUESTAS CONTROLADAS

    if intent == "precio":

        respuesta = (
            "El tratamiento con Tirzepatide cuesta "
            "1.500.000 COP e incluye 12 aplicaciones. "
            "La consulta médica vale 200.000 COP."
        )

    elif intent == "funcionamiento":

        respuesta = (
            "Tirzepatide ayuda a controlar el apetito "
            "y mejorar el metabolismo, facilitando "
            "la pérdida de peso."
        )

    elif intent == "resultados":

        respuesta = (
            "Muchos pacientes logran bajar entre "
            "20% y 25% de su peso "
            "con dieta y seguimiento médico."
        )

    elif intent == "contraindicaciones":

        respuesta = (
            "El tratamiento requiere valoración médica "
            "para revisar contraindicaciones "
            "y seguridad del paciente."
        )

    elif intent == "ubicacion":

        respuesta = (
            "Estamos en Ibagué, Colombia "
            "y realizamos envíos a todo el país."
        )

    elif intent == "lead_caliente":

        respuesta = (
            "¡Perfecto! Podemos evaluar tu caso "
            "y explicarte todo el tratamiento."
        )

    else:

        respuesta = responder(mensaje)

    # Limitar tamaño para TikTok
    respuesta = respuesta[:350]

    # WhatsApp solo cuando conviene
    if intent in ["precio", "lead_caliente"]:
        whatsapp = generar_link()
        respuesta = f"{respuesta}\n\nWhatsApp:\n{whatsapp}"

    return {
        "intent": intent,
        "reply": respuesta
    }