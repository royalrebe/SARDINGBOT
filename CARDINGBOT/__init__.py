import os
import sys
import random
import asyncio

from telethon import TelegramClient
import logging
from os import getenv

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
TOKEN = config("TOKEN", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
OWNER_ID = int(os.environ.get("OWNER_ID", None))



smx = TelegramClient('smx', API_ID, API_HASH).start(bot_token=TOKEN)
