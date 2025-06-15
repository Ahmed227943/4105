import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# الردود التلقائية المدمجة
RESPONSES = {
    "السلام عليكم": "وعليكم السلام ورحمة الله وبركاته",
    "صباح الخير": "صباح الكيك علي عنيك",
    "نمت": "وايه اللي صحاك يا موكوس",
    "بقولك": "اخرس خالص متنطقش",
    "راشد": "ده عيل توتو سيبك منه",
    "بوت": "بوت شمال يلوشك علي وشك",
    "انداري": "من امتي وانت داري يا موكوس",
    "ابشر": "انت فنجري بق وبطنك فاضية وبتتعشي كوسة نية",
    "يا بوت": "كلمة تانية وهاخدك ورا الجبل",
    "مين": "السمين",
    "طارق": "هنبتدي القرف بقي",
    "لوسيفر": "هيييه بتاع العبيد جه"
}

def start(update: Update, context: CallbackContext):
    update.message.reply_text("أهلاً يا نجم! أنا بوت قصف الجبهات 🤖")

def handle_message(update: Update, context: CallbackContext):
    msg = update.message.text.lower()
    for keyword, reply in RESPONSES.items():
        if keyword in msg:
            update.message.reply_text(reply)
            return

def mention_all(update: Update, context: CallbackContext):
    if update.message.chat.type not in ["group", "supergroup"]:
        update.message.reply_text("الأمر ده للجروبات بس يا نجم 💥")
        return
    try:
        members = context.bot.get_chat_administrators(update.message.chat.id)
        mentions = " ".join([f"@{m.user.username}" for m in members if m.user.username])
        update.message.reply_text(f"الكل يسمعني 👇\n{mentions}" if mentions else "مفيش حد يتمنشن يا معلم 😅")
    except:
        update.message.reply_text("معرفتش أمنشنهم.. شكلك عامل فيها أدمين بس 😏")

def main():
    token = os.getenv("TOKEN")
    if not token:
        print("❌ مفيش توكن يا نجم! ضيفه في متغير البيئة TOKEN")
        return

    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("all", mention_all))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("✅ البوت شغال... استعد لقصف الجبهات 🔥")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()