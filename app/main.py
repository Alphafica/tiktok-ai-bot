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
            

             "🔵 Cita de valoración inicial: $200.000 COP." 
             "Esta consulta médica es indispensable ya que es donde el Dr Carlos Giraldo le explica todo el tratamiento: como usar el medicamento, cuanto tiempo, resultados y efectos secundarios y como manejarlos mientras el paciente se adapta y despeja dudas." 

             "🔵 Costo del tratamiento: $1.650.000"

             "🔵 Incluye:
               "1 ampolla de TIRZEPATIDE 60 mg/ml, con la cual se realizan 12 aplicaciones, equivalentes a 3 meses de tratamiento."

            " 🔵 Entrega y acompañamiento:"
               "El medicamento se envía empacado en cadena de frío vía terrestre, garantizando su correcta conservación. Además, recibirás acompañamiento médico durante todo el proceso. "
            

     )

    elif intent == "funcionamiento":
        respuesta =  (
            "💊El medicamento se llama TIRZEPATIDE es actualmente el Análogo GLP1 Más potente"
            "su uso es una inyección subcutánea alrededor del ombligo cada 7 días por 3 meses,"
            "el medicamento es muy potente con una reducción de peso entre el 20% y si "
            "la persona es adherente a dieta rica en proteínas y ejercicio puede bajar más hasta el 25% de su peso ."
            )
        
    elif intent == "bienvenido":
        respuesta =  (
            "Hola✋, Soy el asistente virtual del Dr. Carlos Giraldo👨‍⚕️, a continuación te dejaré algunas opciones "
            "para que puedas obtener la información que deseas."
            
            )    
    elif intent == "ubicacion":
        respuesta =  (
            "💊Estamos Ubicados en la ciudad de Ibagué, Prestamos el "
            "servicio de Teleconsulta a cualquier parte del país."
            
            )    
        
    elif intent == "envio":
        respuesta =  (
            "🚚 Claro que si, el medicamento se envía a tu domicilio por correo certificado, "
            "se te proporciona número de guía e instrucciones inciales."
            
            )      
        

    elif intent == "rebote":
        respuesta =  (
            "💊🔴El Efecto Rebote no se produce por la suspención del medicamento, si no por el "
            "no cumplimiento o mal desarrollo de las recomendaciones médicas para mantener el  "
            "resultado obtenido con el medicamento."
            
            )      

    elif intent == "resultados":
        respuesta =  ( 
                      "✅El medicamento tiene una potencia en reducción de peso entre el 20 al 25% del peso que "
                      "tiene el paciente, incluso puede lograr una mayor reducción si cumple con todas "
                      "las recomedaciones médicas que se explican en la consulta."
                     )
        
    elif intent == "peso":
        respuesta =  ( 
                      "✅El medicamento es muy potente, cuenta con una reducción garantizada entre  "
                      "10 a 12 kilos en los primeros 3 meses de tratamiento siempre y cuando se sigan "
                      "las recomedaciones médicas que se explican en la consulta."
                     )    

    elif intent == "contraindicaciones":
     respuesta = (""
        "1.Antecedentes de cáncer de tiroides,2.Historia de pancreatitis,"
        "3.Alergia a los AGLP-1, 4.No se puede usar en embarazos."
        "5.No se puede usar durante la lactancia"
         )

    elif intent == "lead_caliente":

        whatsapp = generar_link()

        respuesta = (
            "Perfecto 🙌\n\n"
            "Con mucho gusto puedes comunicarte directamente con el equipo médico al whatsapp +573043801974\n\n"
            "se te asignará tu cita médica y brindaremos toda la información que necesites\n\n"
            "¡Espero verte pronto en consulta! 💪⚕️"
            
        )


    else:

        respuesta = responder(mensaje)

    return {
        "reply": respuesta
    }
