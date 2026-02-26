def detectar_intent(texto: str):

    if not texto:
        return "general"

    texto = texto.lower()

    # PRECIO
    if any(x in texto for x in [
        "precio", "cuanto", "vale", "costo", "coste"
    ]):
        return "precio"

    # RESULTADOS
    if any(x in texto for x in [
        "resultado", "bajar", "peso", "antes", "despues"
    ]):
        return "resultados"

    # FUNCIONAMIENTO
    if any(x in texto for x in [
        "funciona", "como funciona", "metodo"
    ]):
        return "funcionamiento"

    # CONTRAINDICACIONES
    if any(x in texto for x in [
        "contra", "riesgo", "efecto", "secundario"
    ]):
        return "contraindicaciones"

    # UBICACION
    if any(x in texto for x in [
        "donde", "ubicacion", "ciudad", "envio"
    ]):
        return "ubicacion"

    # LEAD CALIENTE
    if any(x in texto for x in [
        "quiero", "empezar", "me interesa", "cita"
    ]):
        return "lead_caliente"

    return "general"