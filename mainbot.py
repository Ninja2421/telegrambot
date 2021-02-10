# my api id        2388554
# my api hash      3e30cf236573b82381da92246f9d9586

from telethon import TelegramClient, events
import logging
import json

with open("text/keywords.json") as json_file:
    data = json.load(json_file)
    keyWord = data["keywords"]
    for i in keyWord:
        print(i)

with open("text/receiveFrom.json") as json_file:
    data = json.load(json_file)
    skemmers = data["skemmerMan"]
    print(skemmers)

with open("text/sendTo.json") as json_file:
    data = json.load(json_file)
    sheeps = data["sheeple"]
    print(sheeps)

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
print("Bot Running...")
# Use your own values from my.telegram.org
api_id = 2388554
api_hash = "3e30cf236573b82381da92246f9d9586"


client = TelegramClient("anon", api_id, api_hash)


@client.on(events.NewMessage(from_users=skemmers))
async def my_event_handler(event):
    txt = event.raw_text
    for i in keyWord:
        if i in txt:
            for x in sheeps:
                await client.send_message(x, txt)


client.start()
client.run_until_disconnected()