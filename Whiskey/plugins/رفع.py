import time
import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from Whiskey import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus 

lokrf = []

@app.on_message(
    command(["قفل الرفع","تعطيل الرفع"])
    & filters.group
)
async def lllock(client, message):
    dev = (OWNER_ID)
    haya = int(6947105506)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in haya:
         rotba= "مبرمج السوࢪس" 
    elif  message.from_user.id in dev:
         rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
    
  
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if message.chat.id in lokrf:
        return await message.reply_text(f"**يا {message.from_user.mention}\n الرفع مقفلها من قبل**")
      lokrf.append(message.chat.id)
      return await message.reply_text(f"**تم قفل امر رفع بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")

@app.on_message(
    command(["فتح الرفع","تفعيل الرفع"])
    & filters.group
)
async def idljjopen(client, message):
    dev = (OWNER_ID)
    haya = int(6947105506)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in haya:
         rotba= "مبرمج السوࢪس" 
    elif  message.from_user.id in dev:
         rotba = "مطور اساسي"
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "المالك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "الادمن"
    
   
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in lokrf:
        return await message.reply_text(f"يا {message.from_user.mention}\n الرفع مفتوحه من قبل")
      lokrf.remove(message.chat.id)
      return await message.reply_text(f"**تم تفعيل الرفع بنجاح\n\n بواسطة {rotba} ←{message.from_user.mention}**")
 






klb = []

@app.on_message(command("رفع كلب"))
async def rf3nmla(client, message:Message):
  if not message.reply_to_message.from_user.mention in klb:
    klb.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n كلب من قبل {message.from_user.mention}😂♥️")


@app.on_message(command("ت كلب"))
async def tnzelnmla(client, message:Message):
  if message.reply_to_message.from_user.mention in klb:
    klb.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n من قائمة الكلاب 😂♥️")


@app.on_message(command("المرفوعين كلاب"))
async def nml(client, message):
  kq = ""
  for n in klb:
      kq += n + "\n"
  await message.reply_text(f"**المرفوعين كلاب \n\n{kq}**")

zoj = []


@app.on_message(command("رفع زوجي"))
async def rf3nmla(client, message:Message):
  if not message.reply_to_message.from_user.mention in zoj:
    zoj.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  زوج لـ {message.from_user.mention}😂♥️")


@app.on_message(command("ت زوجي"))
async def tnzelnmla(client, message):
  if message.reply_to_message.from_user.mention in zoj:
    zoj.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n من قائمة المتزوجين رد عزابي 😂♥️**")


@app.on_message(command("المرفوعين المتزوجين"))
async def nml(client, message):
  zq = ""
  for n in zoj:
      zq += n + "\n"
  await message.reply_text(zq)

hth =[]


@app.on_message(command("رفع حثاله"))
async def rf3nmla(client, message:Message):
  if not message.reply_to_message.from_user.mention in hth:
    hth.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n  حثاله من قبل {message.from_user.mention}😂♥️")


@app.on_message(command("ت حثاله"))
async def tnzelnmla(client, message):
  if message.reply_to_message.from_user.mention in hth:
    hth.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**تم تنزيل العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n من قائمة الحثاله 😂♥️**")


@app.on_message(command("المرفوعين حثاله"))
async def nml(client, message):
  hq = ""
  for n in hth:
      hq += n + "\n"
  await message.reply_text(hq)




