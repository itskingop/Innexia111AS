import os
from os import environ


# required vars

TOKEN = os.environ.get("TOKEN", None)
DEMONS = set(int(x) for x in os.environ.get("DEMONS", "").split())
DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "").split())
DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
WOLVES = set(int(x) for x in os.environ.get("WOLVES", "").split())
TIGERS = set(int(x) for x in os.environ.get("TIGERS", "").split())
OWNER_ID = os.environ.get("OWNER_ID", None) 
BOT_USERNAME = os.environ.get("BOT_USERNAME", None) 
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None) 
JOIN_LOGGER = os.environ.get("JOIN_LOGGER", None)
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
DB_URI = os.environ.get("DATABASE_URL")
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_ID = int(os.environ.get("BOT_ID", None))
STRING_SESSION = os.environ.get("STRING_SESSION", None) 
EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
ARQ_API_KEY = ARQ_API


# for heroku deployment only

HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)


# optional // not to change

INFOPIC = bool(os.environ.get("INFOPIC", True))
WEBHOOK = bool(os.environ.get("WEBHOOK", False))
URL = os.environ.get("URL", "")  # Does not contain token
PORT = int(os.environ.get("PORT", 5000))
CERT_PATH = os.environ.get("CERT_PATH")
ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)
DONATION_LINK = os.environ.get("DONATION_LINK")
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", None)
VIRUS_API_KEY = os.environ.get("VIRUS_API_KEY", None)
LOAD = os.environ.get("LOAD", "").split()
NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
STRICT_GMUTE = bool(os.environ.get('STRICT_GMUTE', False))
WORKERS = int(os.environ.get("WORKERS", 8))
BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
ARQ_API = os.environ.get("ARQ_API", None)
TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
AI_API_KEY = os.environ.get("AI_API_KEY", None)
WALL_API = os.environ.get("WALL_API", None)
SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
REDIS_URL = os.environ.get('REDIS_URL', None)
SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
SESSION_NAME = os.getenv("SESSION_NAME")
ARQ_API_URL = "https://thearq.tech"
BL_CHATS = set(int(x) for x in os.environ.get("BL_CHATS", "").split())
