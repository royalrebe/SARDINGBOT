# BIN CHECKER 

import requests
# import types

from telethon.tl import types
from telethon import events
from CARDINGBOT import SUDO_USERS, smx

@smx.on(events.NewMessage(incoming=True, pattern=r".bin(?: |$)(.*)"))
async def binio(message: types.Message):
    if message: types.Message.sender_id in SUDO_USERS:
        await message.answer_chat_action('typing')
        ID = message.from_user.id
        FIRST = message.from_user.first_name
        BIN = message.text[len('.bin '):]
        if len(BIN) < 6:
            return await message.reply(
                       'Send bin not ass'
            )
        r = requests.get(
               f'http://binchk-api.vercel.app/bin={BIN}'
    ).json()
    INFO = f'''
BIN➫ <code>{BIN}</code>
Brand➫ <u>{r["brand"]}</u>
Type➫ <u>{r["type"]}</u>
Level➫ <u>{r["level"]}</u>
Bank➫ <u>{r["bank"]}</u>
Phone➫ <u>{r["phone"]}</u>
Code➫ <u>{r["code"]}</u>
Currency➫ <u>{r["currency"]}</u>
Country➫ <u>{r["country"]}({r["code"]})[{r["flag"]}]</u>
Url➫ <u>{r["url"]}</u>
SENDER: <a href="SMEXXY BOY"</a>
'''
    await message.reply(INFO)
