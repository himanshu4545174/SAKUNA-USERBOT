from telethon import events
import phoenix.client
from phoenix.magic import Magic
import time
magic = Magic()
client = phoenix.client.client
@events.register(events.NewMessage(pattern='\.magic'))
async def magicrun(event):
		time.sleep(0.2)
		for d in magic.magic:
			time.sleep(0.2)
			await event.edit(d)
