import os
import yaml
from telethon import TelegramClient
import logging
# from os import getenv

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

CONFIG = yaml.load(open('config.yml', 'r'), Loader=yaml.SafeLoader)
API_ID = int(os.getenv('API_ID', CONFIG['API_ID']))
API_HASH = int(os.getenv('API_HASH', CONFIG['API_HASH']))
HEROKU_APP_NAME = int(os.getenv('HEROKU_APP_NAME', CONFIG['HEROKU_APP_NAME']))
HEROKU_API_KEY = int(os.getenv('HEROKU_API_KEY', CONFIG['HEROKU_API_KEY']))
TOKEN = int(os.getenv('TOKEN', CONFIG['TOKEN']))
SUDO_USERS = os.getenv('SUDO_USERS', CONFIG['SUDO_USERS'])
OWNER_ID = os.getenv('OWNER_ID', CONFIG['OWNER_ID'])



smx = TelegramClient('smx', API_ID, API_HASH).start(bot_token=TOKEN)
