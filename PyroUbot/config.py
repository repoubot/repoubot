import os

from dotenv import load_dotenv

load_dotenv(".env")

API_ID: int = os.getenv('API_ID', "21290921")
API_HASH: str = os.getenv('API_HASH', "aa536c6c483dcaba1ef80db525bf50c3")

BOT_TOKEN = os.getenv('BOT_TOKEN', "7005648617:AAHrO4dzP2y0jFDdgznbSFyeW3rhahPn8Ow")

OWNER_ID = int(os.getenv('OWNER_ID', "999117814"))

LOGS_MAKER_UBOT = int(os.getenv('LOGS_MAKER_UBOT', " -1002240613244"))

MAX_BOT = int(os.getenv('MAX_BOT', "100"))

RMBG_API = os.getenv("RMBG_API")

OPENAI_KEY = os.getenv("OPENAI_KEY")

MONGO_URL = os.getenv("mongodb+srv://strongubot:<medan2018@strongubot>/?retryWrites=true&w=majority&appName=StrongUbot")
