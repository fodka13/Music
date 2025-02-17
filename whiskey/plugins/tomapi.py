import asyncio
import os
from pyrogram.types import CallbackQuery
from Whiskey import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from Whiskey import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    filters.command("help")
    
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://b.top4top.io/p_2682mb2f41.jpg",
        caption=f"""** 𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀𝙔 𝙎𝙊𝙐𝙍𝘾𝙀 .**\nمرحبا بك عزيزي {message.from_user.mention}\nانا بوت الذكاء الاصطناعي الخاص بسورس الوسكي \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n** 𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀𝙔 𝙎𝙊𝙐𝙍𝘾𝙀 .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة الإستخدام", callback_data="usage"), 
                 ],[
                    InlineKeyboardButton(
                        "𓆩 |𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔", url=f"https://t.me/bp_bp"),
                    InlineKeyboardButton(
                        "حسابي الثاني", url=f"https://t.me/lV_P_Nl"),
                ],[
                
                    InlineKeyboardButton(
                        "★ 𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀𝙔 𝙎𝙊𝙐𝙍𝘾𝙀 .⚡", url=f"https://t.me/Swhiske"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("usage"))
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""** 𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀𝙔 𝙎𝙊𝙐𝙍𝘾𝙀 .**
★¦ اهلا بك عزيزي في قسم الأوامر
★¦ لتتمكن من تشغيل الذكاء الاصطناعي فقط اكتب
★¦ /gpt - لـلـسـؤال آي سـؤال بالـذكـاء الاسـطـناعي

** 𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀𝙔 𝙎𝙊𝙐𝙍𝘾𝙀 .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "العودة", callback_data="back"), 
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def cr_back(_, callback_query: CallbackQuery):
    message = callback_query.message
  
    await message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("طريقة الإستخدام", callback_data="دليل")],
            [InlineKeyboardButton("|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔", url=f"https://t.me/bp_bp"),
             InlineKeyboardButton("حسابي الثاني", url=f"https://t.me/lV_P_Nl")],
            [InlineKeyboardButton("★ 𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀𝙔 𝙎𝙊𝙐𝙍𝘾𝙀 .⚡", url=f"https://t.me/Swhiske")],
        ]
    ))

