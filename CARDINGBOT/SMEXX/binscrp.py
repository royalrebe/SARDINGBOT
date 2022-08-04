import re
import asyncio
import flag

from telethon import events, types, errors
from CARDINGBOT.CONDOM import http
from bs4 import BeautifulSoup as bs
from CARDINGBOT import SUDO_USERS, smx


BIN_CHAT = ""

@smx.on(events.NewMessage(incoming=True, pattern=r".binsr(?: |$)(.*)"))
async def check_incoming_messages(event):
    if event.sender_id in SUDO_USERS:
        me = await smx.get_me()
        if event.sender_id == me.id:
            return
        entities = event.message.entities
        prefixes = ['?', '/', '.', '!']
        m = event.message.message
        if m.startswith(tuple(prefixes)) or len(m) < 25 or event.is_private:
            return
        is_cc = False
        if entities:
        for entity in entities:
            if isinstance(entity, types.MessageEntityBankCard):
                is_cc = True
            if is_cc:
                try:
                    Bin = re.sub(r'[^0-9]', '', m)
                    r = await http.get(f'https://bincheck.io/details/{Bin[:6]}')
                    soup = bs(r, features='html.parser')
                    k = soup.findAll('td', width="65%")
                    MSG = f"""
{m}
BIN: {Bin[:6]}
INFO
{k[0].text}
{k[1].text.strip()}|{k[2].text.strip()}
BANK: {k[3].text.strip()}
{flag.flag(k[8].text)}|{k[10].text.strip()}|{k[8].text.strip()}
COUNTRY: {k[6].text.strip()}"""
                    await asyncio.sleep(3)
                    await smx.send_message(BIN_CHAT, MSG)
                except errors.FloodWaitError as e:
                    print(f'flood wait: {e.seconds}')
                    await asyncio.sleep(e.seconds)
                    await smx.send_message(BIN_CHAT, MSG)