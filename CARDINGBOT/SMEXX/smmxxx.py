from telethon.tl.functions.users import GetFullUserRequest
from telethon import events

from CARDINGBOT import smx, OWNER_ID
from telethon import events

PICC = "https://telegra.ph/file/85fd8d6718c5ded6f4aab.jpg"

@smx.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await event.client.get_me()
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       ssmmd = "Hello, Chutya ! Nice To Meet You,  An Powerfull Spam Bot."
            await smx.client.send_file(TheRiZoeL,
                  PICC,
                  caption=ssmmd)
