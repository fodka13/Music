

import asyncio

import os
import time
import requests
from config import START_IMG_URL,  MUSIC_BOT_NAME
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from Whiskey import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from Whiskey import app
from random import  choice, randint

@app.on_message(
    command(["م1"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم اوامر الفتح والقفل في بوت {MUSIC_BOT_NAME} ميوزك\n
𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀𝙔 𝙎𝙊𝙐𝙍𝘾𝙀 .
**قفل / تعطيل + الامر**

ايدي / صورتي

صور / زوجني

نداء / زخرفه
⩹━⊶⊷⌯𖢿 𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀𝙔 𝙎𝙊𝙐𝙍𝘾𝙀 . 𖢿⌯⊶⊷⋗
**فتح / تفعيل + الامر**

ايدي / صورتي

صور / زوجني

نداء / زخرفه
لتنصيب بوت مشابه تواصل معي فالخاص @bp_bp
**""",


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀𝙔 𝙎𝙊𝙐𝙍𝘾𝙀 .⚡", url=f"https://t.me/HL_BG"),                        
                 ],[
                InlineKeyboardButton(
                        "اغلاق", callback_data="close"),
               ],
          ]
        ),
    )
