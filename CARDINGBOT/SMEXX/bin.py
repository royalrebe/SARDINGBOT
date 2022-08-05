# BIN CHECKER 
import re

from telethon import events
from CARDINGBOT import smx
from CARDINGBOT.CONDOM import http

@smx.on(events.NewMessage(pattern="/bin"))
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
Brand➫ <u>{res["brand"]}</u>
Type➫ <u>{res["type"]}</u>
Level➫ <u>{res["level"]}</u>
Bank➫ <u>{res["bank"]}</u>
Phone➫ <u>{res["phone"]}</u>
Code➫ <u>{res["code"]}</u>
Currency➫ <u>{res["currency"]}</u>
Country➫ <u>{res["country"]}({res["code"]})[{res["flag"]}]</u>
Url➫ <u>{res["url"]}</u>
SENDER: <a href="SMEXXY BOY"</a>
'''
        await event.edit(msg)
    except:
        await event.edit('Failed to parse bin data from api')
