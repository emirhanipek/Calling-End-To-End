import os
import subprocess
import asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# .env dosyasını yükle
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def start_main(update: Update, context: CallbackContext):
    """main.py dosyasını çalıştırır ve kullanıcıyı bilgilendirir."""
    if str(update.message.chat_id) == CHAT_ID:
        await update.message.reply_text("main.py başlatılıyor...")

        # main.py başlat
        process = subprocess.Popen(["python", "main.py"])

        # Kullanıcıyı bilgilendirme mesajlarını 3 saniyede bir gönder
        messages = [
            "Testleriniz yapılıyor...",
            "Biraz daha sabredin, az kaldı...",
            "Hala devam ediyor, yakında tamamlanacak...",
            "Son kontroller yapılıyor...",
            "Raporlar hazırlanıyor...",
            "Bitti Sayılır..."
        ]

        for msg in messages:
            await asyncio.sleep(7)
            await context.bot.send_message(chat_id=CHAT_ID, text=msg)

        await asyncio.sleep(2)
        await context.bot.send_message(chat_id=CHAT_ID, text="Testler tamamlandı ✅")

    else:
        await update.message.reply_text("Yetkiniz yok.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("startmain", start_main))

    print("Bot başlatıldı...")
    app.run_polling()

if __name__ == "__main__":
    main()
