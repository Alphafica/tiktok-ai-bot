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
             "Esta consulta médica es indispensable ya que es donde el Dr Carlos Giraldo le explica todo el tratamiento: como usar el medicamento, cuanto tiempo , resultados y efectos secundarios y como manejarlos mientras el paciente se adapta y despeja dudas.\n\n" 

             "🔵 Costo del tratamiento: $1.650.000\n\n"

             "🔵 Incluye: "
               "1 ampolla de TIRZEPATIDE 60 mg/ml, con la cual se realizan 12 aplicaciones, equivalentes a 3 meses de tratamiento.\n\n"

            " 🔵 Entrega y acompañamiento:"
               "El medicamento se envía empacado en cadena de frío vía terrestre, garantizando su correcta conservación. Además, recibirá acompañamiento médico durante todo el proceso.\n\n "
            

     )

    elif intent == "funcionamiento":
        respuesta =  (
            "La Tirzepatide es un medicamento que ayuda a disminuir el apetito, mejorar el metabolismo y facilitar la pérdida de peso.\n\n"

            "Con seguimiento médico y hábitos adecuados, los pacientes pueden lograr una reducción aproximada del 20% al 25% del peso corporal.\n\n"
            "Durante el proceso recibirás:\n\n "
            "✔️ Seguimiento médico\n\n"
            "✔️ Recomendaciones nutricionales\n\n"
            "✔️ Acompañamiento para lograr resultados sostenibles.\n\n"
            )
        
    elif intent == "bienvenido":
        respuesta =  (
            "Hola✋, Soy el asistente virtual del Dr. Carlos Giraldo👨‍⚕️, a continuación  dejaré algunas opciones "
            "para que pueda obtener la información que desea."
            
            )    
    elif intent == "ubicacion":
        respuesta =  (
            "💊Estamos Ubicados en la ciudad de Ibagué, Prestamos el "
            "servicio de Teleconsulta a cualquier parte del país."
            
            )    
        
    elif intent == "envio":
        respuesta =  (
            "🚚 🔵 Entrega del medicamento"
            "El medicamento se envía empacado en cadena de frío vía terrestre para garantizar su adecuada conservación "
            
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
        "No se debe usar en pacientes que padezcan de \n\n"          
        "1.Antecedentes de cáncer de tiroides\n\n"
        "2.Historia de pancreatitis,\n\n"
        "3.Alergia a los AGLP-1,\n\n"
        "4.No se puede usar en embarazos.\n\n"
        "5.No se puede usar durante la lactancia"
         )

    elif intent == "lead_caliente":

        whatsapp = generar_link()

        respuesta = (

            "📅 Si desea agendar su valoración, escríbanos al whatsapp +573043801974:\n\n "
              "  Nombre completo , edad y ciudad . "
               " y le ayudaremos a programar su cita.\n\n"
                "¡Espero verle pronto en consulta! 💪⚕️"
            
        )


    else:

        respuesta = responder(mensaje)

    return {
        "reply": respuesta
    }
