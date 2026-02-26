def generar_link():

    telefono = "573019140372"

    mensaje = "Hola vengo desde TikTok quiero información"

    mensaje = mensaje.replace(" ", "%20")

    link = f"https://wa.me/{telefono}?text={mensaje}"

    return link