import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from CARDINGBOT.utils import chumt
import logging
from telethon import events
from . import smx

os.system("pip install httpx")

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "CARDINGBOT/SMEXX/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        chumt(plugin_name.replace(".py", ""))

print("SMMEXY BOT IS START")        

if __name__ == "__main__":
    smx.run_until_disconnected()
