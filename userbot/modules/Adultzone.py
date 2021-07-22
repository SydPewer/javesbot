# credits to Syd
# ported to Pawanbir by @I_AM_PAWANBIR
# will be adding more soon

import asyncio
import os
import urllib

import requests

from userbot import *
from userbot.utils import *


@bot.on(admin_cmd("sax$"))
async def boobs(event):
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("Dlt This Mr❗")
    await asyncio.sleep(0.5)
    await a.edit("⚠️ Warning ⚠️")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


@bot.on(admin_cmd("sex$"))
async def butts(event):
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "butts.jpg")
    a = await event.reply("Finding But Warning❗")
    await asyncio.sleep(0.5)
    await a.edit("⚠️ Warning ⚠️")
    nsfw = requests.get("http://api.obutts.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


CMD_HELP.update(
    {
        "adultzone": "**Plugin : **`Bad-zone`\
        \n\n**Syntax : **`.sax`\
        \n**Usage :** Warning..Searchs and sends random B××Bs image\
        \n\n**Syntax :**`.sex`\
        \n**Usage :** Warning..Searchs and sends random Butts image\
        \n\n\n     __**⚠️ Warning 18+ ⚠️**__"
    }
)
