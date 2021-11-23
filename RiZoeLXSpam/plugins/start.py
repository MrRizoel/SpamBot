import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from .. import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10

PM_START_TEXT = """
I <b>✨ **Welcome** \n
💭 **ᴛʜɪs ɪs ᴛʜᴇ sᴘᴀᴍ ᴜsᴇʀʙᴏᴛ ᴏғ [ʀɪᴢᴏᴇʟ x](https://t.me/RiZoeLX) ᴜsᴇʀ **

💡 **𝘾𝙡𝙞𝙘𝙠 𝙊𝙣 𝙗𝙚𝙡𝙤𝙬 𝙗𝙪𝙩𝙩𝙤𝙣𝙨 𝙁𝙤𝙧 𝙍𝙀𝙋𝙊 𝘼𝙉𝘿 𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𝘾𝙃𝘼𝙉𝙉𝙀𝙇**

**𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝑩𝒚 [𝑹𝒊𝒁𝒐𝒆𝑳 𝑿️](https://t.me/RiZoeLX)**</b>"""


@Riz.on(events.NewMessage(pattern="/start"))
@Riz2.on(events.NewMessage(pattern="/start"))
@Riz3.on(events.NewMessage(pattern="/start"))
@Riz4.on(events.NewMessage(pattern="/start"))
@Riz5.on(events.NewMessage(pattern="/start"))
@Riz6.on(events.NewMessage(pattern="/start"))
@Riz7.on(events.NewMessage(pattern="/start"))
@Riz8.on(events.NewMessage(pattern="/start"))
@Riz9.on(events.NewMessage(pattern="/start"))
@Riz10.on(events.NewMessage(pattern="/start"))
async def start(event):              
   if event.is_private:
       await event.client.send_file(RIZ_IMG,
                caption=PM_START_TEXT, 
                buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/RiZoeLX"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/DNHxHELL")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/MrRizoel/RiZoeLXSpam")
        ])