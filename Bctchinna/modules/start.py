from telethon import events, Button
 
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10
from Bctchinna.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("𝗛𝗘𝗟𝗣 𝗔𝗡𝗗 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦", data="help_back")
        ],
        [
        Button.url("𝗨𝗣𝗗𝗔𝗧𝗘𝗦", "https://t.me/iam_chinna"),
        Button.url("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", "https://t.me/iam_chinna")
        ],
        [
        Button.url("𝗥𝗘𝗣𝗢", "https://github.com/")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**𝗛𝗘𝗬 [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝗜 𝗔𝗠  [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **✦ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗗 𝗕𝗬 :~ [Chinna](https://t.me/iam_chinna)**\n\n"
        TEXT += f"» **𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗦𝗣𝗔𝗠 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 :** `3.2`\n"
        TEXT += f"» **𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡 𝗩𝗘𝗥𝗦𝗜𝗢𝗡:** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://telegra.ph/file/05522e13c97752efe5e75.png",
                caption=TEXT, 
                buttons=PythonButton)
