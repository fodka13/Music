import asyncio
import time
from pyrogram.types import *
from pyrogram import filters, Client
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from pyrogram.enums import ChatType, ParseMode
import config
import requests
import redis, re

from config import (OWNER_ID ,
		     USER_OWNER,
	         MUSIC_BOT_NAME,
	         SUPPORT_CHANNEL,
	         BOT_TOKEN,
	         BANNED_USERS)
from strings import get_command, get_string
from Whiskey import Telegram, YouTube, app
from Whiskey.misc import SUDOERS, _boot_
from Whiskey.plugins.playlist import del_plist_msg
from Whiskey.plugins.sudoers import sudoers_list
from Whiskey.utils.database import (add_served_chat,
                                       add_served_user,
                                       get_served_chats,
                                       get_served_users,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from Whiskey.utils.decorators.language import LanguageStart
from Whiskey.utils.formatters import get_readable_time
from Whiskey.utils.inline import (help_pannel, private_panel,
                                     start_pannel)
r = redis.Redis(
    host="127.0.0.1",
    port=6379,)
token = (BOT_TOKEN)
loop = asyncio.get_running_loop()
owner = (OWNER_ID,6947105506) 
bot_id = token.split(":")[0]
try:
	open(f"Users{bot_id}.json","r")
except FileNotFoundError:
	open(f"Users{bot_id}.json","w")
try:
	open(f"sudo{bot_id}.json","r")
except FileNotFoundError:
	open(f"sudo{bot_id}.json","w")
try:
	open(f"maindevs{bot_id}.json","r")
except FileNotFoundError:
	open(f"maindevs{bot_id}.json","w")
try:
	open(f"maindevsVII{bot_id}.json","r")
except FileNotFoundError:
	open(f"maindevsVII{bot_id}.json","w")
try:
	open(f"groups{bot_id}.json","r")
except FileNotFoundError:
	open(f"groups{bot_id}.json","w")
try:
	open(f"band{bot_id}.json","r")
except FileNotFoundError:
	open(f"band{bot_id}.json","w")
try:
	open(f"links{bot_id}.json","r")
except FileNotFoundError:
	open(f"links{bot_id}.json","w")
try:
	open(f"channel{bot_id}.json","r")
except FileNotFoundError:
	open(f"channel{bot_id}.json","w")
try:
	open(f"devchannel{bot_id}.json","r")
except FileNotFoundError:
	open(f"devchannel{bot_id}.json","w")
try:
	open(f"devuser{bot_id}.json","r")
except FileNotFoundError:
	open(f"devuser{bot_id}.json","w")
try:
	open(f'owner{bot_id}.json','r')
except FileNotFoundError:
	f = open(f'owner{bot_id}.json','w')
	f.write(str(owner))
@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.private
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            dev = (OWNER_ID, 6947105506)
          
		
            keyboard = help_pannel(_)
            Owneruser = ReplyKeyboardMarkup([
[("الاوامر"),("السورس")],[("المطور"),("مبرمج السورس"),("/مساعده")],
[("غنيلي"),("كت"),("صور")],
[("اذكار"),("مميز القروبات"),("ذكاء اصتناعي")],
[("•---- حذف الكيبورد -----•")]
], resize_keyboard=True)
  
					
            if message.from_user.id in dev:
		           
                   await message.reply(f"**𖢿 | : مرحبا عزيزي المطور الاساسي {message.from_user.mention}\n𖢿 | : اليك ازرار التحكم بالاقسام\n𖢿 | : تستطيع التحكم بجميع الاقسام فقط اضغط على القسم الذي تريده**",reply_markup=OwnerM)
                        
 
            else:  
                   await message.reply_text(f"**اهلا عزيزي {message.from_user.mention}\n\n في بوت الميوزك {MUSIC_BOT_NAME} الخاص بي @{USER_OWNER} \n\n هذا بوت تشغيل اغاني وبه الكثير من المميز القروبات الجميله \n\n ارفع البوت مشرف وهايرفعك مالك ويرفع المشرفين تلقائي**",reply_markup=Owneruser)
                   return await message.reply_photo(
                       photo=config.START_IMG_URL,
                       caption=_["help_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard
            )

            

        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        
        if name[0:3] == "sta":
            m = await message.reply_text(
                f"🥱 يتم جلب الاحصائي القروبات الخاصه لـ {config.MUSIC_BOT_NAME} sᴇʀᴠᴇʀ."
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🔗[قناة السورس](https://t.me/HL_BG) ** ᴩʟᴀʏᴇᴅ {count} ᴛɪᴍᴇs**\n\n"
                    else:
                        msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(
                    None, get_stats
                )
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ضغط ستارت على البوت <code>دخل على قائمة المطورين</code>\n\n**ايديه:** {sender_id}\n**اسمه:** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text(
                    "ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ ʟʏʀɪᴄs."
                )
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name == "verify":
            await message.reply_text(f"ʜᴇʏ {message.from_user.first_name},\nشكرا لوثوقك في انا  {config.MUSIC_BOT_NAME}, تم تخزين بيان القروباتك اللازمه يمكنك التشغيل الان")
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention}ضغط ستارت على البوت <code>تحقق من نفسه</code>\n\n**ايديه:** {sender_id}\n**اسمه:** {sender_name}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("دقيقه يقلبي وحانجيب البيان القروبات")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[
                    0
                ]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
😲**جلب المعلوم القروبات**😲
 𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀𝙔 𝙎𝙊𝙐𝙍𝘾𝙀 .
📌 **العنوان:** {title}

⏳ **المده:** {duration} دقيقه
👀 **المشاهد القروبات:** `{views}`
⏰ **نشرت في:** {published}
🎥 **القناه:** {channel}
📎 **رابط القناه:** [عرض القناه]({channellink})
🔗 **الرابط:** [مشاهده في اليوتيوب]({link})
 𓏺˛ 𝙒𝙃𝙄𝙎𝙆𝙀𝙔 𝙎𝙊𝙐𝙍𝘾𝙀 .
💖 بحث بواسطة {config.MUSIC_BOT_NAME}"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="• ʏᴏᴜᴛᴜʙᴇ •", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="• قناة السورس •", url="https://t.me/HL_BG"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=key,
            )
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention}ضغط ستارت على البوت<code>جلب المعلوم القروبات</code>\n\n**ايديه:** {sender_id}\n**اسمه:** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        if config.START_IMG_URL:
            try:
                dev = (OWNER_ID)

                Owneruser = ReplyKeyboardMarkup([
[("الاوامر"),("السورس")],[("المطور"),("مبرمج السورس"),("/مساعده")],
[("غنيلي"),("كت"),("صور")],
[("اذكار"),("مميز القروبات"),("ذكاء اصتناعي")],
[("•---- حذف الكيبورد -----•")]
], resize_keyboard=True)		    
            
                if message.from_user.id in dev:
                   await message.reply_text(f"**𖢿 | : مرحبا عزيزي المطور الاساسي {message.from_user.mention}\n𖢿 | : اليك ازرار التحكم بالاقسام\n𖢿 | : تستطيع التحكم بجميع الاقسام فقط اضغط على القسم الذي تريده**",reply_markup=OwnerM)
                else:  
                   await message.reply_text(f"**اهلا عزيزي {message.from_user.mention}\n\n في بوت الميوزك {MUSIC_BOT_NAME} الخاص بي @{USER_OWNER} \n\n هذا بوت تشغيل اغاني وبه الكثير من المميز القروبات الجميله \n\n ارفع البوت مشرف وهايرفعك مالك ويرفع المشرفين تلقائي**",reply_markup=Owneruser)
                   return await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_2"].format(
                        config.MUSIC_BOT_NAME
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
    
            except:
                await message.reply_text(
                    _["start_2"].format(config.MUSIC_BOT_NAME),
                    reply_markup=InlineKeyboardMarkup(out),
                )
        else:
            await message.reply_text(
                _["start_2"].format(config.MUSIC_BOT_NAME),
                reply_markup=InlineKeyboardMarkup(out),
            )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} ضغط ستارت في البوت.\n\n**ايديه:** {sender_id}\n**اسمه:** {sender_name}",
            )
        

@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.group
    & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    OWNER = OWNER_ID[0]
    out = start_pannel(_, app.username, OWNER)
    return await message.reply_photo(
               photo=config.START_IMG_URL,
               caption=_["start_1"].format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**بوت ميوزك خاص**\n\فقط الدردش القروبات المصرح بها بواسطة المطور."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                OWNER = OWNER_ID[0]
                out = start_pannel(_, app.username, OWNER)
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            return
        except:
            return

def is_user(id):
	result = False
	file = open(f"Users{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result

def is_dev(id):
	result = False
	file = open(f"sudo{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result
	
def del_all_sudo():
	open(f"sudo{bot_id}.json","w")

def del_all_main():
	open(f"maindevs{bot_id}.json","w")

def del_all_mainVII():
	open(f"maindevsVII{bot_id}.json","w") 
	
def del_all_ban():
	open(f"band{bot_id}.json","w")

def is_main_dev(id):
	result = False
	file = open(f"maindevs{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result
	
def is_main_devVII(id):
	result = False
	file = open(f"maindevsVII{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result
	
def is_band(id):
	result = False
	file = open(f"band{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return  result
	
def is_group(id):
	result = False
	file = open(f"groups{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result

def add_user(id):
	file = open(f"Users{bot_id}.json","a")
	file.write("{}\n".format(id))

def show_channel() -> str:
	with open(f"channel{bot_id}.json","r") as file:
		return file.readline()

def add_channel(chat_id):
	with open(f"channel{bot_id}.json","w") as file:
		file.write(chat_id)

def del_channel():
	open(f"channel{bot_id}.json","w")

def get_bot_owner() -> int:
	with open("owner{bot_id}.json","r") as file:
		return file.readline()
		
def set_bot_owner(user_id:int):
	with open(f"owner{bot_id}.json","w") as file:
		file.write(str(user_id))

def show_devchannel() -> str:
	with open(f"devchannel{bot_id}.json","r") as file:
		return file.readline()

def add_devchannel(chat_id):
	with open(f"devchannel{bot_id}.json","w") as file:
		file.write(chat_id)

def del_devchannel():
	open(f"devchannel{bot_id}.json","w")


def show_devuser() -> str:
	with open(f"devuser{bot_id}.json","r") as file:
		return file.readline()

def add_devuser(chat_id):
	with open(f"devuser{bot_id}.json","w") as file:
		file.write(chat_id)

def del_devuser():
	open(f"devuser{bot_id}.json","w")


OwnerM = ReplyKeyboardMarkup([
[("رفع مالك"),("تنزيل مالك"),("المالكين"),("حذف المالكين")],
[("/الغاء")], 
[("◍ قسم الاحصائي القروبات ◍")],
[("/احصائي القروبات"),("احصائي القروبات البوت"),("نسخه الكل")],
[("عرض المجموع القروبات"),("عدد المجموع القروبات"),("نسخه المجموع القروبات"),("روابط المجموع القروبات")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("عدد الاساسيين"),("عدد الاعضاء"),("عدد المحظورين"),("عدد المطورين")], 
[("نسخه الاساسيين"),("السورس"),("نسخه المحظورين"),("نسخه المطورين")],
[("/اضف فار"),("/حذف فار"),("/جلب فار")],
[("/حدد"),("/مكالمات"),("/تحديث")],
[("-")],
[("قسم الاذاعه")],
[("ذيع"),("-"),("اذاعه")],
[("اذاعه الاعضاء"),("اذاعه المجموع القروبات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموع القروبات"),("توجيه محظورين")],
[("الغاء")], 


[("◍ قسم الاساسيين"),("◍ قسم المطورين"),("◍ قسم الحظر ◍")],
[("رفع مطور اساسي"),("رفع مطور"),("حظر عضو")],
[("ت ثانوي"),("رفع ثانوي"),("الغاء حظر عضو")],
[("مبرمج السورس"),("المطور"),("عرض المحظورين")],
[("حذف الاساسيين"),("حذف المطورين"),("حذف المحظورين")],
[("الغاء")],
[("صور"),("كت"),("غنيلي")],

[("◍ قسم الاشتراك ◍"),("◍ قسم معرف المطور ◍"),("◍ قسم المطور ◍")],
[("عرض قناة الاشتراك"),("عرض معرف المطور"),("عرض قناة المطور")],
[("اضف قناة اشتراك اجباري"),("اضافه معرف المطور"),("اضافه قناه المطور")],
[("حذف قناه الاشتراك"),("حذف معرف المطور"),("حذف قناه المطور")],
[("الغاء")], 
[("•---- حذف الكيبورد -----•")]
], resize_keyboard=True
					)

mainSudoVIIM = ReplyKeyboardMarkup([
[("•---- حذف الكيبورد -----•")],
[("◍ قسم الاحصائي القروبات ◍")],
[("الاحصائي القروبات")],
[("عرض المجموع القروبات"),("عدد المجموع القروبات"),("نسخه المجموع القروبات"),("نسخه للكل")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("عدد الاساسيين"),("عدد الاعضاء"),("عدد المحظورين"),("عدد المطورين")], 
[("نسخه الاساسيين"),("نسخه الاعضاء"),("نسخه المحظورين"),("نسخه المطورين")],

[("-")], 

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموع القروبات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموع القروبات"),("توجيه محظورين")],
[("الغاء")], 


[("◍ قسم الاساسيين"),("◍ قسم المطورين"),("◍ قسم الحظر ◍")],
[("رفع مطور اساسي"),("رفع مطور"),("حظر عضو")],
[("تنزيل مطور اساسي"),("تنزيل مطور"),("الغاء حظر عضو")],
[("عرض المطورين الاساسيين"),("عرض المطورين"),("عرض المحظورين")],
[("حذف الاساسيين"),("حذف المطورين"),("حذف المحظورين")],
[("الغاء")],

[("◍ قسم الاشتراك ◍"),("◍"),("◍ قسم المطور ◍")],
[("عرض قناة الاشتراك"),("-"),("عرض قناة المطور")],
[("اضف قناة اشتراك اجباري"),("-"),("اضافه قناه المطور")],
[("حذف قناه الاشتراك"),("-"),("حذف قناه المطور")],
[("الغاء")], 
[("•---- حذف الكيبورد -----•")]
], resize_keyboard=True
					)


main_dev_key = ReplyKeyboardMarkup([
[("•---- حذف الكيبورد -----•")],
[("◍ قسم الاحصائي القروبات ◍")],
[("الاحصائي القروبات")],
[("عرض المجموع القروبات"),("عدد المجموع القروبات"),("نسخه المجموع القروبات"),("نسخه للكل")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("عدد الاساسيين"),("عدد الاعضاء"),("عدد المحظورين"),("عدد المطورين")], 
[("نسخه الاساسيين"),("نسخه الاعضاء"),("نسخه المحظورين"),("نسخه المطورين")],

[("-")], 

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموع القروبات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموع القروبات"),("توجيه محظورين")],
[("الغاء")], 


[("◍ قسم الاساسيين"),("◍ قسم المطورين"),("◍ قسم الحظر ◍")],
[("رفع مطور اساسي"),("رفع مطور"),("حظر عضو")],
[("تنزيل مطور اساسي"),("تنزيل مطور"),("الغاء حظر عضو")],
[("عرض المطورين الاساسيين"),("عرض المطورين"),("عرض المحظورين")],
[("الغاء")],

[("•---- حذف الكيبورد -----•")]
], resize_keyboard=True)

sudo_keyboard = ReplyKeyboardMarkup([
[("•---- حذف الكيبورد -----•")],
[("◍ قسم الاحصائي القروبات ◍")],
[("الاحصائي القروبات"),("نسخه")],
[("عرض المجموع القروبات"),("نسخه للقروب القروبات"),("عدد  القروبات")],
[("عرض روابط المجموع القروبات"),("نسخه للمحظورين")],
[("عرض الاعضاء"),("عرض المطورين")], 
[("عدد الاعضاء"),("عدد المطورين")], 
[("نسخه الاعضاء"),("نسخه المطورين")],

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموع القروبات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموع القروبات"),("توجيه محظورين")],
[("الغاء")], 

[("◍ قسم الحظر ◍")],
[("حظر عضو "),("الغاء حظر عضو"),("عرض المحظورين")],
[("•---- حذف الكيبورد -----•")]
], resize_keyboard=True)








start_buttons = InlineKeyboardMarkup([[
InlineKeyboardButton("ch",url=f"https://t.me/{show_devchannel()}")
]])


New_Member = """**
دخل عضو جديد للبوت 🪄🪄

᥀︙حسابة : {} 
᥀︙ايديه : `{}`

Time : {} .

**"""
	
dev_ch_bu = InlineKeyboardMarkup([[
InlineKeyboardButton("Dev",user_id=owner),
InlineKeyboardButton("Ch",url=f"https://t.me/{show_devchannel()}")
]])




@app.on_message(filters.command("احصائي القروبات البوت","")&filters.private & ~filters.group)
async def __count(c:Client , m:Message):
	user = m.from_user.id
	OWNER = (OWNER_ID)
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if  str(user) == '6947105506' or  str(user) in sudo or str(user) in mainSudoVII or (user) in OWNER:
		users = len(open(f"Users{bot_id}.json","r").readlines())
		groups = len(open(f"groups{bot_id}.json","r").readlines())
		sudos = len(open(f"sudo{bot_id}.json","r").readlines())
		main = len(open(f"maindevs{bot_id}.json","r").readlines())
		bans = len(open(f"band{bot_id}.json","r").readlines())
		
		msg = f"""
		**◍ Bot Status : **
			
		├ المستخدمين : {users} 
		├ المطورين الاساسيين: {sudos} 
		├ المجموع القروبات : {groups} 
		├ المطورين : {main} 
		├ المحظورين  {bans} 
		
		√ """
		return await m.reply(msg,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("close",callback_data="close")]]))
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
@app.on_message(filters.command("نسخه الكل","")&filters.private)
async def __get_copy(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	OWNER = (OWNER_ID)
	if  str(user) == '6947105506' or  str(user) in sudo or str(user) in mainSudoVII or (user) in OWNER:
		users = open(f"Users{bot_id}.json","rb")
		groups = open(f"groups{bot_id}.json","rb")
		band = open(f"band{bot_id}.json","rb")
		sudos = open(f"sudo{bot_id}.json","rb")
		main = open(f"maindevs{bot_id}.json","rb")
		
		uc = len(open(f"Users{bot_id}.json","r").readlines())
		gc = len(open(f"groups{bot_id}.json","r").readlines())
		bc = len(open(f"band{bot_id}.json","r").readlines())
		sc = len(open(f"sudo{bot_id}.json","r").readlines())
		mc = len(open(f"maindevs{bot_id}.json","r").readlines())
		
		cc = await m.reply("**◍ جاري جلب النسخه الاحتياطية \n√**")
		time.sleep(3)
		await cc.delete()
		try:
			await m.reply_document(document=users,caption=f"**Bot users : {uc} √**")
		except:
			await m.reply("**◍ لم يقم اي عضو بالدخول الي بوتك √**")
		try:
			await m.reply_document(document=groups,caption=f"**Bot groups : {gc} √**")
		except:
			await m.reply("**◍ لم يتم تفعيل اي مجموع القروبات في بوتك √**")
		try:
			await m.reply_document(document=band,caption=f"**Band users : {bc} √**")
		except:
			await m.reply("**◍ لا يوجد اعضاء محظورين في البوت √**")
		try:
			await m.reply_document(document=sudos,caption=f"**Sudo users : {sc} √**")
		except:
			await m.reply("**◍ لا يوجد مطورين في البوت √**")
		try:
			await m.reply_document(document=main,caption=f"**Main devs : {mc} √**")
		except:
			await m.reply("**◍ لا يوجد مطورين اساسيين في البوت √**")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
@app.on_message(filters.command("عدد المجموع القروبات","")&filters.private)
async def get_groups_count(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	OWNER = (OWNER_ID)
	if  str(user) == '6947105506' or  str(user) in sudo or str(user) in mainSudoVII or (user) in OWNER:
		leng = len(open(f"groups{bot_id}.json","r").readlines())
		if leng == 0:
			return await m.reply("**◍ لا توجد مجموع القروبات تم تفعيلها في البوت √**")
		return await m.reply(f"**◍ تم تفعيل {leng} مجموعة في بوتك \n√**")
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
@app.on_message(filters.command("اضف قناة اشتراك اجباري","")&filters.private)
async def AddKey(c:Client,m:Message):
	user = m.from_user.id
	OWNER = (OWNER_ID)
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if  str(user) == '6947105506'or int(user) in OWNER:
		ask = await m.chat.ask('**معرف القناه بدون @**')
		if ask.text == "الغاء":
			await ask.request.delete()
			await ask.delete()
			await m.reply(f"**تم الالغاء**")
			return
		if '@' in ask.text:
			return await m.reply('**المعرف بدون @**')
		if "ا" in ask.text:
			return await m.reply('لم يتم** التعرف**')
		add_channel(chat_id=ask.text)
		await m.reply('**تم وضع {} قناة اشتراك √**'.format(ask.text))
		return
@app.on_message(filters.command("عرض قناة الاشتراك","")&filters.private)
async def ShowKey(c:Client,m:Message):
	user = m.from_user.id
	OWNER = (OWNER_ID)
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if  str(user) == '6947105506' or str(user) in mainSudoVII or (user) in OWNER:
	    return await m.reply("الامر تحت الصيانه")

@app.on_message(filters.command("توجيه الاعضاء",prefixes=""))
async def memcommands__(c,m):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	OWNER = (OWNER_ID)
	if  str(user) == '6947105506' or  str(user) in sudo or str(user) in mainSudoVII or (user) in OWNER:
		await m.delete()
		ask = await m.reply(chat,"**• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة  القروباتصال، ملف )**")
		inputText = ask.text 
		
		if inputText == "الغاء":
			await m.reply("**تم الغاء الاذاعه بالتوجيه**")
		
		else:
			users = open(f"Users{bot_id}.json","r")
			
			for user in users:
				try:
					await ask.forward (int(user)
					)
				except:
					pass
			
			us = len(open(f"Users{bot_id}.json","r").readlines())
			await app.send_message(chat,f"**تم الاذاعه بالتوجيه الي **:\n {us} من الاعضاء")
@app.on_message(filters.command("•---- حذف الكيبورد -----•","")&filters.private)
async def del_keyboard(c:Client,m:Message):

	
	await m.reply("**◍ تم حذف الكيبورد بنجاح  /start\n√**",reply_markup=ReplyKeyboardRemove())







@app.on_message(filters.command("^نسخه المحظورين$","")&filters.private)
async def get_copy___band(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	OWNER = (OWNER_ID)
	if  str(user) == '6947105506' or  str(user) in sudo or str(user) in mainSudoVII or (user) in OWNER:
		file = open(f"band{bot_id}.json","rb")
		lenb = len(open(f"band{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري جلب نسخه للمحظورين √**")
		time.sleep(2)
		if lenb == 0:
			return await l.edit("**◍ لم يتم حظر اي عضو من استخدام البوت √**")
		await l.delete()
		await m.reply_document(document=file,caption=f"**Band users {lenb} √")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")




@app.on_message(filters.command("^عدد المحظورين$","")&filters.private)
async def countofuserBan(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	OWNER = (OWNER_ID)
	if  str(user) == '6947105506' or  str(user) in sudo or str(user) in mainSudoVII or (user) in OWNER:
		l = await m.reply("**◍ جاري حساب عدد الاعضاء √**")
		lens = len(open(f"band{bot_id}.json","r").readlines())
		time.sleep(.5)
		if lens == 0:
			return await l.edit("**◍ لم يدخل اي عضو للبوت حتي الآن √**")
		return await l.edit(f"**◍ عدد اعضاء بوتك {lens} √**")
	return await m.reply("**◍ انت لست مطور في البوت \n√**")


@app.on_message(filters.command("عرض المطورين الاساسيين","")|filters.command("عرض الاساسيين","") &filters.private)
async def ShowMain(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	
	OWNER = (OWNER_ID)
	if  str(user) == '6947105506' or  str(user) in mainSudo or str(user) in mainSudoVII or (user) in OWNER:
		file = open(f"maindevs{bot_id}.json","r")
		lens = len(open(f"maindevs{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري عرض المطورين الاساسيين √**")
		x = 1
		text = "**Bot Main Users **:\n\n"
		for su in file:
			text += f"{x} - {su}"
			x += 1
		time.sleep(1)
		if lens == 0:
			return await l.edit("**◍ لم يتم رفع مطورين اساسيين في البوت √**")
		return await l.edit(text=text)
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
	
@app.on_message(filters.command("^نسخه الاساسيين$","")&filters.private)
async def get_MainSudo(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	
	OWNER = (OWNER_ID)
	if  str(user) == '6947105506' or  str(user) in mainSudo or str(user) in mainSudoVII or (user) in OWNER:
		file = open(f"maindevs{bot_id}.json","rb")
		lenb = len(open(f"maindevs{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري جلب نسخه للمطورين الاساسيين√**")
		time.sleep(2)
		if lenb == 0:
			return await l.edit("**◍ لم تقم برفع اي مطور اساسي في البوت√**")
		await l.delete()
		await m.reply_document(document=file,caption=f"**Sudo Main Users {lenb} √")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")


@app.on_message(filters.command("حذف قناه الاشتراك","")&filters.private)
async def DellKey(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	OWNER = (OWNER_ID)
	if  str(user) == '6947105506' or  str(user) in sudo or str(user) in mainSudoVII or (user) in OWNER:
         del_channel()
	     
         await m.reply("تم حذف قناة الاشتراك")
@app.on_message(filters.command("اضافه معرف المطور","")&filters.private)
async def AddDevUser(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	OWNER = (OWNER_ID)
	if  (user) in OWNER:
		ask = await m.reply('**معرف المطور بدون @**')
		if ask.text == "الغاء":
			await ask.request.delete()
			await ask.delete()
			await m.reply(f"**تم الالغاء**")
			return
		if '@' in ask.text:
			return await m.reply('**المعرف بدون @**')
		if 'اضافه'in ask.text:
			return await m.reply('**لم يتم التعرف**')
		add_devuser(chat_id=ask.text)
		await m.reply('**تم وضع معرف المطور @{} √**'.format(ask.text))
		return
@app.on_message(filters.command("عرض معرف المطور","")&filters.private)
async def ShowDevUser(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or (user) in owner:
	    return await m.reply("الامر تحت الصيانه")
@app.on_message(filters.command("حذف معرف المطور","")&filters.private)
async def DellDevUser(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or (user) in owner:
         del_devuser()
	     
         await m.reply("معرف المطور")
	 


@app.on_message(filters.command("اذاعه للكل",prefixes=""))
async def AllCommand__(c,m:Message):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or (user) in owner:
		await m.delete()
		ask = await m.reply(chat,"**• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة  القروباتصال، ملف )**")
		inputText = ask.text 
		
		if inputText == "الغاء":
			await m.reply("**تم الغاء الاذاعه**")
		else:
			users = open(f"Users{bot_id}.json","r")
			groups = open(f"groups{bot_id}.json","r")
			bans = open(f"band{bot_id}.json","r")
			
			for user in users:
				try:
					await ask.copy(int(user),
					inputText,
					reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
				
			for group in groups:
				try:
					await ask.copy(int(group),
					inputText,
					reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
			
			for ban in bans:
				try:
					await ask.copy(int(ban),
					inputText,
					reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
				
			x1 = len(open(f"Users{bot_id}.json","r").readlines())
			x2 = len(open(f"band{bot_id}.json","r").readlines())
			x3 = len(open(f"groups{bot_id}.json","r").readlines())
			
			
			await app.send_message(chat,
			f"**تم الاذاعه الي** : \n\n {x1} من الأعضاء \n {x2} من المحظورين \n {x3} من المجموع القروبات")
@app.on_message(filters.command("اذاعه الاعضاء",prefixes=""))
async def memcommands__(c,m:Message):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or (user) in owner:
		await m.delete()
		ask = await m.reply(chat,"**• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة  القروباتصال، ملف )**")
		inputText = m.text 
		
		if inputText == "الغاء":
			await m.reply("**تم الغاء الاذاعه**")
		
		else:
			users = open(f"Users{bot_id}.json","r")
			
			for user in users:
				try:
					await ask.copy(int(user),
					inputText, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
			
			us = len(open(f"Users{bot_id}.json","r").readlines())
			await app.send_message(chat,f"**تم الاذاعه الي **: \n {us} من الاعضاء")
@app.on_message(filters.command("اذاعه المجموع القروبات",prefixes=""))
async def memcommands__(c,m:Message):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or (user) in owner:
		await m.delete()
		ask = await m.reply(chat,"**• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة  القروباتصال، ملف )**")
		inputText = ask.text 
		
		if inputText == "الغاء":
			await m.reply("**تم الغاء الاذاعه**")
		
		else:
			group = open(f"groups{bot_id}.json","r")
			
			for user in group:
				try:
					await ask.copy(int(user),
					inputText, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
                    url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
			
			gr = len(open(f"groups{bot_id}.json","r").readlines())
			await app.send_message(chat,f"**تم الاذاعه الي **: \n {gr} من  القروبات")
