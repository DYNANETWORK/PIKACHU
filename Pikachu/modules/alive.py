from telethon import events, Button, custom
import re, os
from Pikachu.events import register
from Pikachu import telethn as tbot
from Pikachu import telethn as tgbot
PHOTO = "https://telegra.ph/file/0ac1f1b5c5b2376a14f3f.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**β‘ I,m β­π PΝIΝKΝAΝCΝHΝUΝ πβ­** \n\n"
  PIKACHU += "**β‘ I'm Working Properly**\n\n"
  PIKACHU += "**β‘ β­π PΝIΝKΝAΝCΝHΝUΝ πβ­ : 2.2 LATEST**\n\n"
  PIKACHU += "**β‘ My Master :** [HACKER](t.me/HID_DENBOY)\n\n"
  PIKACHU += "**β‘ Telethon Version : 1.23.0**\n\n"
  PIKACHU += "**β‘ Kali Linux : yes**\n\n"
  PIKACHU += "**β‘ Python : 3.9.7**\n\n"
  PIKACHU += "**β‘ Database status : Functional**\n\n"
  BUTTON = [[Button.url("πππππππ", "https://t.me/PIKACHU_X_SPPORT"), Button.url("πππΏπΌππ", "https://t.me/PIKACHU_X_SUPPORT")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)


__mod_name__ = "AliveβοΈ"
