

import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from Whiskey import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from Whiskey import app
from random import  choice, randint



@app.on_message(
    command(["مميز القروبات","مميز القروبات"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم مميز القروبات سورس وسكي ميوزك\n
𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀� �𝙎𝙊𝙐𝙍𝘾� .

**𖢿قايمه مميز القروبات سورس وسكي الليبي

𖢿ميزه ⦂ المطور بيجيب المطور البوت 
𖢿ميزه ⦂ تبيه بفتح+قفل  المكالمات ه
𖢿ميزه ⦂ ترحيب دخول و خروج الاعضاء 
𖢿ميزه ⦂ قروب بيجيب الرابط+ايدي
𖢿ميزه ⦂ قول البوت بيقول بالكلمه اللي بتقولها 
𖢿ميزه ⦂ الالعاب +كت+تويت+العاب متطوره
𖢿ميزه ⦂ تلغراف ميديا بردعالصوره
𖢿ميزه ⦂ ايدي بالرد بالصوره
𖢿ميزه ⦂ صورتي يرد بالصوره ونسبه
𖢿ميزه ⦂ اذاعه خاص+بالتثبيت+بالمساعد+عام
𖢿ميزه ⦂ الصوتيه..ف  المكالمات ه
𖢿ميزه ⦂ نزول تلقائي للمساعد لعدم وجود حد ف المكالمات ه
𖢿ميزه ⦂ بث مباشر للقنو القروبات 
𖢿ميزه ⦂ اسمي بيجب الاسم
𖢿ميزه ⦂ سورس بيجب السورس
𖢿ميزه ⦂ حظر+كتم ميوزك
𖢿ميزه ⦂ كشف
𖢿ميزه ⦂ منشن لكل الاعضاء
𖢿ميزه ⦂ انا من
𖢿ميزه ⦂ رتبتي
𖢿ميزه ⦂ مبرمج
𖢿ميزه ⦂ المنشئ+المالك
𖢿ميزه ⦂ الاحصائي القروبات
𖢿ميزه ⦂ كيب المطور من خلاله تتحكم في الحساب المساعد
𖢿ميزه ⦂ الاذكار
𖢿ميزه ⦂ تبيه بوقت صلاه
𖢿ميزه ⦂ دعوه في مكالمه
𖢿ميزه ⦂  دعوه فالخاص متاع البوت
𖢿ميزه ⦂ تنبيه..بانضمام بوت في  القروبات
𖢿ميزه ⦂ غنيلي 
𖢿ميزه ⦂ بايو
𖢿ميزه ⦂ خروج المساعد من قروب القروبات لعدم تقطيع صوت..البوت
𖢿ميزه ⦂ اسال/اصراحه
𖢿ميزه ⦂ نكت
𖢿ميزه ⦂ ذكاء اصتناعي 
𖢿ميزه ⦂ مميز القروبات. بيجبلك مميز القروبات موجوده فسورس 
𖢿ميزه ⦂ رفع و تنزيل مطور 
𖢿ميزه ⦂ افلام
𖢿ميزه ⦂مكالمات القروبات النشطه+مجموع القروبات البوت شغال فيها
𖢿ميزه ⦂ اساله دينيه
𖢿ميزه ⦂ من في  المكالمات ه+تعرف من ف المكالمات ه و عددهم
𖢿ميزه ⦂ الرابط+رابط مجموعه
𖢿افتح  المكالمات ه يفتح  المكالمات ه
مطـور الســـورس الوسـڪي الليبي
𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀� �𝙎𝙊𝙐𝙍𝘾� .
لتنصيب بوت مشابه تواصل معي فالخاص @bp_bp
**""",


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀� �𝙎𝙊𝙐𝙍𝘾� .⚡", url=f"https://t.me/HL_BG"),                        
                 ],[
                InlineKeyboardButton(
                        "اغلاق", callback_data="close"),
               ],
          ]
        ),
    )

