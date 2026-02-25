import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")
DATABASE_URL = "sqlite:///./bot.db"