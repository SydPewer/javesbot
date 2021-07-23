from userbot import bot
from userbot.utils import admin_cmd

@bot.on(admin_cmd(pattern=r"deployme"))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Click [Here](https://heroku.com/deploy?template=https://github.com/JSydPewer/javesbot/blob/main) to open source code for deploying your own Javes : SD userbot.")
