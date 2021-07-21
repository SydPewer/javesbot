#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

print("an online StringSession generator")


print("t ==> Telethon (docs.telethon.dev)")
print("Telethon UserBot ==> https://github.com/SydPewer/javesbot")


def Javes2():
    print("you selected Telethon")
    # (c) https://t.me/TelethonChat/37677
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    APP_ID = int(input("Your API ID: "))
    API_HASH = input("Your API HASH: ")
    with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
        session_str = client.session.save()
        s_m = client.send_message("me", session_str)
        s_m.reply(
            "Here Is Your String Session https://replit.com/@SydPewer/Javes-20-String-session?v=1 \nPlease subscribe https://t.me/JavesSD "
        )
        print("check Saved Messages For String ")


Javes2()
