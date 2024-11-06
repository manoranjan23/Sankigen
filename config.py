from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "27884171"))
API_HASH = getenv("API_HASH", "abe760b5d6b33e15c676577d6ae4a06a")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Somu:Somu@somu.xbkiklu.mongodb.net/?retryWrites=true&w=majority&appName=Somu")

OWNER_ID = int(getenv("OWNER_ID", 7070591202))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OFFICIAL_TSGROUP")
