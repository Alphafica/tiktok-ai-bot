def detectar_intent(texto: str):

    if not texto:
        return "general"

    texto = texto.lower()

    if any(x in texto for x in ["precio", "cuanto", "vale", "costo"]):
        return "precio"

    if any(x in texto for x in ["interesa", "quiero", "empezar"]):
        return "lead_caliente"

    if any(x in texto for x in ["funciona", "resultado", "bajar"]):
        return "resultado"

    if any(x in texto for x in ["envio", "ciudad", "donde"]):
        return "ubicacion"

    return "general"