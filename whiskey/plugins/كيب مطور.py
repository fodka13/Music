from pyrogram import Client, filters
from pyrogram.types import (
    Message, InlineKeyboardMarkup,
    InlineKeyboardButton, ReplyKeyboardMarkup,
    CallbackQuery, ReplyKeyboardRemove
)
import os
import time
import json
import requests
from config import BOT_TOKEN, OWNER_ID

app = Client("my_bot", bot_token=BOT_TOKEN)

# ------ إعدادات الأساسية ------
bot_id = BOT_TOKEN.split(":")[0]
DATA_FILES = {
    'users': f'Users{bot_id}.json',
    'sudo': f'sudo{bot_id}.json',
    'main_devs': f'maindevs{bot_id}.json',
    'main_devs_vii': f'maindevsVII{bot_id}.json',
    'groups': f'groups{bot_id}.json',
    'banned': f'band{bot_id}.json',
    'links': f'links{bot_id}.json',
    'channel': f'channel{bot_id}.json',
    'dev_channel': f'devchannel{bot_id}.json',
    'dev_user': f'devuser{bot_id}.json',
    'owner': f'owner{bot_id}.json'
}

# ------ تهيئة الملفات ------
for file in DATA_FILES.values():
    if not os.path.exists(file):
        with open(file, 'w') as f:
            if file == DATA_FILES['owner']:
                f.write(str(OWNER_ID))
            elif file == DATA_FILES['channel']:
                f.write('')

# ------ الدوال المساعدة ------
def read_channel():
    try:
        with open(DATA_FILES['channel'], 'r') as f:
            return f.read().strip()
    except:
        return ''

def write_channel(channel_name):
    with open(DATA_FILES['channel'], 'w') as f:
        f.write(channel_name)

def read_data(file_key):
    with open(DATA_FILES[file_key], 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def write_data(file_key, data):
    with open(DATA_FILES[file_key], 'w') as f:
        json.dump(data, f)

def add_item(file_key, item):
    data = read_data(file_key)
    if str(item) not in data:
        data.append(str(item))
        write_data(file_key, data)

def remove_item(file_key, item):
    data = read_data(file_key)
    if str(item) in data:
        data.remove(str(item))
        write_data(file_key, data)

def is_in(file_key, item):
    return str(item) in read_data(file_key)

def is_authorized(user_id):
    return (
        user_id == OWNER_ID or
        is_in('main_devs_vii', user_id) or
        is_in('main_devs', user_id) or
        is_in('sudo', user_id)
    )

# ------ الكيبوردات ------
start_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("قناة السورس", url="https://t.me/Swhiske")]
])

sudo_keyboard = ReplyKeyboardMarkup([
    ["الاحصائيات", "نسخة احتياطية"],
    ["عرض المحظورين", "حظر عضو"],
    ["إذاعة عامة", "توجيه عام"],
    ["حذف الكيبورد"]
], resize_keyboard=True)

# ------ Handlers ------
@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    user_id = message.from_user.id
    mention = message.from_user.mention
    
    # التحقق من الاشتراك الإجباري
    channel = read_channel()
    if channel:
        try:
            member = await client.get_chat_member(channel, user_id)
            if member.status in ['left', 'kicked']:
                await message.reply(
                    "⛔ يجب الاشتراك في القناة أولاً!\n@{}".format(channel),
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("انضم للقناة", url=f"https://t.me/{channel}")],
                        [InlineKeyboardButton("تأكيد الاشتراك", callback_data="check_sub")]
                    ])
                )
                return
        except Exception as e:
            print(f"خطأ في التحقق من القناة: {e}")

    if is_in('banned', user_id):
        return await message.reply("❌ أنت محظور من استخدام البوت!")

    # تحديد الصلاحيات
    if user_id == OWNER_ID:
        await message.reply("👑 مرحبا مالك البوت!", reply_markup=sudo_keyboard)
    elif is_in('main_devs_vii', user_id):
        await message.reply("💎 مرحبا المطور الأساسي!", reply_markup=sudo_keyboard)
    elif is_in('main_devs', user_id):
        await message.reply("🔧 مرحبا المطور!", reply_markup=sudo_keyboard)
    elif is_in('sudo', user_id):
        await message.reply("🛠️ مرحبا المسؤول!", reply_markup=sudo_keyboard)
    else:
        add_item('users', user_id)
        await message.reply(f"👋 أهلا {mention}!", reply_markup=start_keyboard)

@app.on_callback_query(filters.regex("check_sub"))
async def check_sub(client, callback: CallbackQuery):
    user_id = callback.from_user.id
    channel = read_channel()
    
    try:
        member = await client.get_chat_member(channel, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            await callback.message.delete()
            await client.send_message(user_id, "✅ تم التحقق بنجاح، يمكنك استخدام البوت الآن!")
        else:
            await callback.answer("لم تنضم للقناة بعد!", show_alert=True)
    except Exception as e:
        await callback.message.reply("❗ فشل في التحقق من الاشتراك")

# ------ أوامر الإدارة ------
@app.on_message(filters.command("اذاعة") & filters.private)
async def broadcast(client, msg: Message):
    if not is_authorized(msg.from_user.id):
        return
    
    if not msg.reply_to_message:
        return await msg.reply("❗ يرجى الرد على الرسالة المراد إذاعتها")
    
    users = read_data('users') + read_data('groups')
    total = len(users)
    success = 0
    
    progress = await msg.reply(f"📤 جاري الإذاعة... (0/{total})")
    
    for user_id in users:
        try:
            await msg.reply_to_message.copy(int(user_id))
            success += 1
        except:
            pass
        await progress.edit(f"📤 جاري الإذاعة... ({success}/{total})")
        time.sleep(0.1)
    
    await progress.edit(f"✅ تم الإرسال بنجاح إلى {success}/{total}")

@app.on_message(filters.command("حظر") & filters.private)
async def ban_user(client, msg: Message):
    if not is_authorized(msg.from_user.id):
        return
    
    try:
        user_id = int(msg.text.split()[1])
        add_item('banned', user_id)
        await msg.reply(f"✅ تم حظر {user_id}")
    except:
        await msg.reply("❗ يرجى إدخال آيدي صحيح")

@app.on_message(filters.command("الغاء حظر") & filters.private)
async def unban_user(client, msg: Message):
    if not is_authorized(msg.from_user.id):
        return
    
    try:
        user_id = int(msg.text.split()[1])
        remove_item('banned', user_id)
        await msg.reply(f"✅ تم إلغاء حظر {user_id}")
    except:
        await msg.reply("❗ يرجى إدخال آيدي صحيح")

@app.on_message(filters.command("رفع مطور") & filters.user(OWNER_ID))
async def add_sudo(client, msg: Message):
    try:
        user_id = int(msg.text.split()[1])
        add_item('sudo', user_id)
        await msg.reply(f"✅ تم رفع {user_id} كمطور")
    except:
        await msg.reply("❗ يرجى إدخال آيدي صحيح")

@app.on_message(filters.command("تنزيل مطور") & filters.user(OWNER_ID))
async def remove_sudo(client, msg: Message):
    try:
        user_id = int(msg.text.split()[1])
        remove_item('sudo', user_id)
        await msg.reply(f"✅ تم تنزيل {user_id} من المطورين")
    except:
        await msg.reply("❗ يرجى إدخال آيدي صحيح")

@app.on_message(filters.command("الاحصائيات") & filters.private)
async def stats(client, msg: Message):
    if not is_authorized(msg.from_user.id):
        return
    
    stats_msg = f"""
📊 إحصائيات البوت:
👥 المستخدمين: {len(read_data('users'))}
👥 المطورين: {len(read_data('sudo'))}
🚫 المحظورين: {len(read_data('banned'))}
🗂️ المجموعات: {len(read_data('groups'))}
    """
    await msg.reply(stats_msg)

@app.on_message(filters.command("نسخة") & filters.private)
async def backup(client, msg: Message):
    if not is_authorized(msg.from_user.id):
        return
    
    files = [DATA_FILES['users'], DATA_FILES['groups'], DATA_FILES['sudo']]
    for file in files:
        await msg.reply_document(file, caption=f"نسخة احتياطية - {os.path.basename(file)}")

# ------ تشغيل البوت ------
if __name__ == "__main__":
    print("✅ البوت يعمل...")
    app.run()