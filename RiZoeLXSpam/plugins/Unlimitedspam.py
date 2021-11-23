import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, SUDO_USERS

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)


@Riz.on(events.NewMessage(pattern=".uspam"))
@Riz2.on(events.NewMessage(pattern=".uspam"))
@Riz3.on(events.NewMessage(pattern=".uspam"))
@Riz4.on(events.NewMessage(pattern=".uspam"))
@Riz5.on(events.NewMessage(pattern=".uspam"))
@Riz6.on(events.NewMessage(pattern=".uspam"))
@Riz7.on(events.NewMessage(pattern=".uspam"))
@Riz8.on(events.NewMessage(pattern=".uspam"))
@Riz9.on(events.NewMessage(pattern=".uspam"))
@Riz10.on(events.NewMessage(pattern=".uspam"))
async def unlimitedspam(event):
  if event.sender_id in SMEX_USERS:
    try:
      op = event.text[7:]
      x = None
      while x == None:
        await event.client.send_message(event.chat, op)
        await asyncio.sleep(2)
    except Exception as e:
      await event.reply("Oops!! Something went wrong, Report In @DNHxHELl\n\n" + str(e))