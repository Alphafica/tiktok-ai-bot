from .config import WHATSAPP_NUMBER


def generar_link():

    texto = "Hola vengo desde TikTok quiero información"

    texto = texto.replace(" ", "%20")

    return f"https://wa.me/{WHATSAPP_NUMBER}?text={texto}"