def detectar_intent(texto: str):

    if not texto:
        return "general"

    texto = texto.lower()

    # PRECIO
    if any(x in texto for x in [
        "precio", "cuanto", "vale", "costo", "coste"
    ]):
        return "precio"
    
    # BIENVENIDO
    if any(x in texto for x in [
        "hola", "Hola", "Info", "buenos", "buenas","dias","tardes","noches", "deseo","informacion"
    ]):
        return "bienvenido"
    
    # REBOTE
    if any(x in texto for x in [
        "efecto", "rebote", "peso", "antes", "despues"
    ]):
        return "rebote"

    # RESULTADOS
    if any(x in texto for x in [
        "resultado", "bajar", "antes", "despues"
    ]):
        return "resultados"
    # PESO
    if any(x in texto for x in [
        "efectivo","baja","peso"
    ]):
        return "peso"

    # FUNCIONAMIENTO
    if any(x in texto for x in [
        "funciona", "como funciona", "metodo"
    ]):
        return "funcionamiento"

    # CONTRAINDICACIONES
    if any(x in texto for x in [
        "contra", "riesgo", "contraindicacion", "secundario","contraindicaciones"
    ]):
        return "contraindicaciones"

    # UBICACION
    if any(x in texto for x in [
        "donde", "ubicacion", "ciudad", "envio","estan","ubicados","consultorio", "ubicación"
    ]):
        return "ubicacion"

    # LEAD CALIENTE
    if any(x in texto for x in [
        "quiero", "empezar", "me interesa", "cita", "Solicitar cita"
    ]):
        return "lead_caliente"

    return "general"