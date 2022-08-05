from telethon.tl.functions.users import GetFullUserRequest
from telethon import events

from CARDINGBOT import smx, OWNER_ID
from telethon import events

PICC = "https://telegra.ph/file/85fd8d6718c5ded6f4aab.jpg"

@smx.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await event.client.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝐑𝐈𝐙𝐎𝐄𝐋 𝐗](https://t.me/RiZoeLX)**"
       if smx.sender_id == OWNER_ID:
            await event.client.send_file(TheRiZoeL,
                  PICC,
                  caption=ownermsg)
       else:
            await smx.client.send_file(TheRiZoeL,
                  PICC,
                  caption=usermsg)
                
