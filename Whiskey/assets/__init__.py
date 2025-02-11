from pyrogram import Client, filters
import random

# قائمة تضم بعض أسماء المستخدمين الوهمية.
FAKE_VISITORS = [
    "أحمد", "سارة", "محمد", "فاطمة", "خالد", "ريم", "يوسف", "ليلى", "علي", "نور"
]

# أنشئ التطبيق مع بيان القروبات API الخاصة ببوت Telegram.
# تأكد من استبدال api_id و api_hash بالقيم الخاصة بك.
app = Client("my_bot", api_id=22520725, api_hash="88230118ef743288ef6e17c686f114cf", bot_token="7806023225:AAHgM7vLZ60jnUn3xZZc3egtZKr846nfTSs")

# عند إرسال الأمر /simulate يقوم البوت بمحاكاة "زوار" ملفك الشخصي.
@app.on_message(filters.command("simulate", prefixes="/"))
def simulate_visitors(client, message):
    # توليد عدد عشوائي من الزوار بين 1 و 5.
    num_visitors = random.randint(1, 5)
    # اختيار أسماء زوار عشوائية من القائمة.
    visitors = random.sample(FAKE_VISITORS, num_visitors)
    # تجميع الأسماء في رسالة واحدة.
    result = "\n".join(visitors)
    message.reply_text("زوار ملفك الشخصي (محاكاة):\n" + result)

app.run()

