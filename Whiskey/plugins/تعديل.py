from config import OWNER_ID
import asyncio
from pyrogram import Client, filters
from Whiskey import app
import random
# إذا كنت تستخدم أمرًا مخصصًا يمكنك إما استبداله بـ filters.command 
# أو تعديل الاستدعاء حسب ما هو مناسب في إصدارك.
from pyrogram.types import Message

# قائمة تخزن أرقام المحادث القروبات (chat id) التي تم تعطيل التعديل بها.
iddof = []

# أمر تعطيل التعديل
@app.on_message(filters.command("تعطيل التعديل", prefixes=["/", "!", "."]) & filters.group)
async def iddlock(client: Client, message: Message):
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    # في الإصدار الأول، يكون status عبارة عن سلسلة نصيّة: "administrator" أو "creator"
    if member.status == "administrator":
        rotba = "الادمن"
    elif member.status == "creator":
        rotba = "المالك"
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")
    
    # تأكد من عدم تفعيل التعطيل مسبقًا
    if message.chat.id in iddof:
        return await message.reply_text(f"يا {message.from_user.mention}\nالتعديل معطل من قبل")
    
    iddof.append(message.chat.id)
    return await message.reply_text(f"تم تعطيل التعديل بنجاح\n\n بواسطة {rotba} ← {message.from_user.mention}")

# أمر تفعيل التعديل
@app.on_message(filters.command("تفعيل التعديل", prefixes=["/", "!", "."]) & filters.group)
async def idljjopen(client: Client, message: Message):
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member.status == "administrator":
        rotba = "الادمن"
    elif member.status == "creator":
        rotba = "المالك"
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")
    
    # تأكد من أن التعديل معطل قبل محاولة تفعيله
    if message.chat.id not in iddof:
        return await message.reply_text(f"يا {message.from_user.mention}\nالتعديل مفعل من قبل")
    
    iddof.remove(message.chat.id)
    return await message.reply_text(f"تم تفعيل التعديل بنجاح\n\n بواسطة {rotba} ← {message.from_user.mention}")

# عند تعديل الرسالة يتم حذفها إذا كان التعديل معطل في تلك المحادثة
@app.on_edited_message()
async def delete_edited_message(client: Client, message: Message):
    if message.chat.id in iddof:
        # في Pyrogram 1 تستخدم الخاصية message.message_id للحصول على معرف الرسالة
        await client.delete_messages(chat_id=message.chat.id, message_ids=message.message_id)
