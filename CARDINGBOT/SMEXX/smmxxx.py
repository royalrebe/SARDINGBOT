from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest

from CARDINGBOT import SUDO_USERS, smx

BOT_PIC = "https://telegra.ph/file/2ea23de03e268b1d026c2.jpg"

@smx.on(events.NewMessage(pattern="^/start"))
async def start(event):
    starkbot = await smx.get_me()
    bot_id = starkbot.first_name
    bot_username = starkbot.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    vent = event.chat_id
    starttext = f"𝙷𝙴𝙻𝙻𝙾, {firstname} ! 𝙽𝙸𝙲𝙴 𝚃𝙾 𝙼𝙴𝙴𝚃 𝚈𝙾𝚄, 𝚆𝙴𝙻𝙻 𝙸 𝙰𝙼 {bot_id}, 𝙰𝙽 𝙿𝙾𝚆𝙴𝚁𝙵𝚄𝙻𝙻 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙱𝙾𝚃.\n\nMy [➤ ᗰᗩՏTᗴᖇ](tg://user?id={bot.uid}) \n\n 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚃𝙰𝙻𝙺 | 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃. \n\n 𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙲𝙰𝙽 𝙳𝙴𝙿𝙻𝙾𝚈 𝙵𝚁𝙾𝙼 𝙱𝚄𝚃𝚃𝙾𝙽 𝙱𝙴𝙻𝙾𝙴.\n\n𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 [『𝐃𝐀𝐑𝐊𝐖𝐄𝐁』](https://t.me/DARK_WEB_UB)"
    if event.sender_id == bot.uid:
        await smx.send_file(
            event.chat_id,
            BOT_PIC,
            message=f"𝙷𝙸 𝙼𝙰𝚂𝚃𝙴𝚁, 𝙸𝚃𝚂 𝙼𝙴 {bot_id}, 𝚈𝙾𝚄𝚁 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃! \n\n 𝚆𝙷𝙰𝚃 𝚈𝙾𝚄 𝚆𝙰𝙽𝙽𝙰 𝙳𝙾 𝚃𝙾𝙳𝙰𝚈 ?",
            buttons=[
                [
                    custom.Button.inline("📊 sᴛᴀᴛs", data="users"),
                ]
                [
                    Button.url(
                        "ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", f"t.me/{bot_username}?startgroup=true"
                    )
                ],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await smx.send_file(
            event.chat_id,
            BOT_PIC,
            message=starttext,
            link_preview=False,
            buttons=[
                [custom.Button.inline("ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ᴅᴀʀᴋᴡᴇʙ", data="deploy")],
                [Button.url("Sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", "https://t.me/DARK_WEB_BOT_SUPPORT")],
            ],
        )
