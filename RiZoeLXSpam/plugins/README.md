# EXTRA PLUGINS

```python
from .. import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, SUDO_USERS
from telethon import events


@Riz.on(events.NewMessage(pattern=".hi"))
@Riz2.on(events.NewMessage(pattern=".hi"))
@Riz3.on(events.NewMessage(pattern=".hi"))
@Riz4.on(events.NewMessage(pattern=".hi"))
@Riz5.on(events.NewMessage(pattern=".hi"))
@Riz6.on(events.NewMessage(pattern=".hi"))
@Riz7.on(events.NewMessage(pattern=".hi"))
@Riz8.on(events.NewMessage(pattern=".hi"))
@Riz9.on(events.NewMessage(pattern=".hi"))
@Riz10.on(events.NewMessage(pattern=".hi"))
async def hi(e):
    if e.sender_id in SUDO_USERS:
        event = await e.reply(text, parse_mode=None, link_preview=None )
        await event.edit(f"``**HELLO**``")
```
