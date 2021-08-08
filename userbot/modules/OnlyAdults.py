#@its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince 

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd
from userbot import CMD_HELP
from . import *


@borg.on(admin_cmd(pattern="xnxx_video?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Processing...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "💋2016 Videolar🔞{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```You have blocked @SeXn1bot, unblock and try again```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)

#Social distancing....

@borg.on(admin_cmd(pattern="xnxx_pic?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Processing...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "♨️Old photo👙{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```You have blocked @SeXn1bot, unblock and try again```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)

#Social distancing....

@borg.on(admin_cmd(pattern="xnxx_gif?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Processing...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "🔞Uz_sex♨️{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```You have blocked @SeXn1bot, unblock and try again```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)
            
CMD_HELP.update(
    {
        "OnlyAdults": "**Plugin : **`OnlyAdults`\
        \n\n**Syntax : **`.xnxx_video`\
        \n**Usage :** Try it yourself🤪\
        \n\n**Syntax :**`.xnxx_pic`\
        \n**Usage :** Try it yourself🤪\
        \n\n**Syntax :**`.xnxx_gif`\
        \n**Usage :** Try it yourself🤪\
        \n\n\n     __**⚠️ Warning 18+ Kids stay away ⚠️**__"
    }
)

#@its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince @its_Prince 
