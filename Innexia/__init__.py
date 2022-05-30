from config import *
from config import OWNER_ID, BOT_USERNAME, EVENT_LOGS as ERROR_LOG
import logging
import os
import sys
import time
import spamwatch
from redis import StrictRedis

import telegram.ext as tg
from pyrogram import Client, errors
from telethon import TelegramClient
from telethon.sessions import MemorySession
from telethon.sessions import StringSession
from Python_ARQ import ARQ
from aiohttp import ClientSession

StartTime = time.time()

# logging enable 

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

    from config import *

    TOKEN = TOKEN
    OWNER_ID = OWNER_ID    
    try:
        OWNER_ID = int(OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = JOIN_LOGGER
    ALLOW_CHATS = ALLOW_CHATS
    try:
        DRAGONS = set(int(x) for x in DRAGONS or [])
        DEV_USERS = set(int(x) for x in DEV_USERS or [])
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in DEMONS or [])
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in WOLVES or [])
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in TIGERS or [])
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    EVENT_LOGS = EVENT_LOGS
    WEBHOOK = WEBHOOK
    URL = URL
    PORT = PORT
    CERT_PATH = CERT_PATH
    API_ID = API_ID
    API_HASH = API_HASH
    BOT_USERNAME = BOT_USERNAME
    OWNER_USERNAME = OWNER_USERNAME
    DB_URI = SQLALCHEMY_DATABASE_URI
    MONGO_DB_URI = MONGO_DB_URI
    ARQ_API = ARQ_API_KEY
    ARQ_API_URL = ARQ_API_URL
    HEROKU_API_KEY = HEROKU_API_KEY
    HEROKU_APP_NAME = HEROKU_APP_NAME
    TEMP_DOWNLOAD_DIRECTORY = TEMP_DOWNLOAD_DIRECTORY
    OPENWEATHERMAP_ID = OPENWEATHERMAP_ID
    BOT_ID = BOT_ID
    API_ID = API_ID
    API_HASH = API_HASH
    STRING_SESSION = STRING_SESSION
    VIRUS_API_KEY = VIRUS_API_KEY
    DONATION_LINK = DONATION_LINK
    LOAD = LOAD
    NO_LOAD = NO_LOAD
    DEL_CMDS = DEL_CMDS
    STRICT_GBAN = STRICT_GBAN
    WORKERS = WORKERS
    BAN_STICKER = AN_STICKER
    ALLOW_EXCL = ALLOW_EXCL
    CASH_API_KEY = CASH_API_KEY
    TIME_API_KEY = TIME_API_KEY
    AI_API_KEY = AI_API_KEY
    WALL_API = WALL_API
    SUPPORT_CHAT = SUPPORT_CHAT
    SPAMWATCH_SUPPORT_CHAT = SPAMWATCH_SUPPORT_CHAT
    SPAMWATCH_API = SPAMWATCH_API
    INFOPIC = INFOPIC

    try:
        BL_CHATS = set(int(x) for x in Config.BL_CHATS or [])
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")

DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(5391883908)
DEV_USERS.add(5351941642)

if not SPAMWATCH_API:
    sw = None
    LOGGER.warning("SpamWatch API key missing! recheck your config.")
else:
    try:
        sw = spamwatch.Client(SPAMWATCH_API)
    except:
        sw = None
        LOGGER.warning("Can't connect to SpamWatch!")


updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("INNEXIA", API_ID, API_HASH)
pbot = Client("innexiaBot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
dispatcher = updater.dispatcher
ubot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
aiohttpsession = ClientSession()
# ARQ Client
LOGGER.info("[ARQ CLIENT] Checking Arq Connections...")

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)


DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from Innexia.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
