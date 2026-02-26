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
            "El tratamiento cuesta 1.500.000 COP, incluye 1 ampolla de  12 aplicaciones "
            "durante 3 meses. La consulta médica cuesta 200.000 COP."
        )

    elif intent == "funcionamiento":
        respuesta =  (
            "💊El medicamento se llama TIRZEPATIDE es actualmente el Análogo GLP1 Más potente"
            "su uso es una inyección subcutánea alrededor del ombligo cada 7 días por 3 meses,"
            "el medicamento es muy potente con una reducción de peso entre el 20% y si "
            "la persona es adherente a dieta rica en proteínas y ejercicio puede bajar más hasta el 25% de su peso ."
            )

    elif intent == "resultado":
        respuesta = responder_intent("resultado")

    elif intent == "contraindicaciones":
     respuesta = (""
        "1.Antecedentes de cáncer de tiroides"
        "2.Historia de pancreatitis"
        "3.Alergia a los AGLP-1"
        "4.No se puede usar en embarazos."
        "5.No se puede usar durante la lactancia"
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
        "reply": respuesta
    }