# BIN CHECKER 
import re

from telethon import events
from CARDINGBOT import smx
from CARDINGBOT.CONDOM import http

@smx.on(events.NewMessage(pattern="^/bin"))
async def srbin(event):
    BIN = event.message.message[len('/bin '):]
    reply_msg = await event.get_reply_message()
    if reply_msg:
        BIN = reply_msg.message
    try:
        _BIN = re.sub(r'[^0-9]', '', BIN)
        _res = await http.get(f'http://binchk-api.vercel.app/bin={_BIN}')
        res = _res.json()
        msg = f'''
BIN➫ <code>{BIN}</code>
Brand➫ <u>{re["brand"]}</u>
Type➫ <u>{re["type"]}</u>
Level➫ <u>{re["level"]}</u>
Bank➫ <u>{re["bank"]}</u>
Phone➫ <u>{re["phone"]}</u>
Code➫ <u>{re["code"]}</u>
Currency➫ <u>{re["currency"]}</u>
Country➫ <u>{re["country"]}({re["code"]})[{re["flag"]}]</u>
Url➫ <u>{re["url"]}</u>
SENDER: <a href="SMEXXY BOY"</a>
'''
        await event.edit(msg)
    except:
        await event.edit('Failed to parse bin data from api')
