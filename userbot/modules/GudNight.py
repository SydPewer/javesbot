from telethon import events
import asyncio
import os
import sys
from userbot.utils import admin_cmd
import random
from userbot import bot as borg

text1 = "Listen to the night sky; the mockingbird always sings you my lullaby."
text2 = "The day is over, the night is here, know that I love you today and forever, my dear."
text3 = "Each night, I hope the moon is large and bright and you will be happy and right. When you turn off the light, keep in mind that I am dreaming of you."
text4 = "Good night. May you fall asleep in the arms of a dream so beautiful you’ll cry when you awake."
text5 = "Take a deep breath and sleep tight while dreaming of me. Sweet dreams."
text6 = "Off to my land of dreams and fantasies, Good Night and sweet dreams."
text8 = "A good laugh and a long sleep are the best cures in the doctor's book."
text9 = "Loving you is like breathing. How can I stop it? Good Night. See you in dreams world."
text10 = "Stars light, stars bright, you are the onlystar i see tonight ! good night my friend."


@borg.on(admin_cmd(outgoing=True, pattern="gnn"))

async def _(event):

    if event.fwd_from:
        return
    # await event.edit("̀ˋSending a beautiful quote for you..`")
    await asyncio.sleep(0)
    x=(random.randrange(0,5))
    if x==1:
        await borg.send_message(event.chat_id,text1)
    if x==2:
        await borg.send_message(event.chat_id,text2)
    if x==3:
        await borg.send_message(event.chat_id,text3)
    if x==4:
        await borg.send_message(event.chat_id,text4)
    if x==5:
        await borg.send_message(event.chat_id,text5)
    if x==6:
        await borg.send_message(event.chat_id,text6)
    if x==7:
        await borg.send_message(event.chat_id,text7)
    if x==8:
        await borg.send_message(event.chat_id,text8)
    if x==9:
        await borg.send_message(event.chat_id,text9)
    if x==10:
        await borg.send_message(event.chat_id,text10)
        
