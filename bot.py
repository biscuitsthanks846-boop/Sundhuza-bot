from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import logging

# Your token and channel
TOKEN = "8997723619:AAF8n8e55Db3a-GJS6bmhl85EP6czuwi_BA"
CHANNEL = "@Gracey34g"

logging.basicConfig(level=logging.INFO)

async def handle_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message:
        return

    caption = message.caption or "🔥 New content available 🔥"

    try:
        if message.photo:
            # Highest quality photo
            photo = message.photo[-1]
            await context.bot.send_photo(
                chat_id=CHANNEL,
                photo=photo.file_id,
                caption=caption
            )
        elif message.video:
            await context.bot.send_video(
                chat_id=CHANNEL,
                video=message.video.file_id,
                caption=caption
            )
        else:
            await message.reply_text("Please send a photo or video.")
            return

        await message.reply_text("✅ Posted to channel!")
    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO | filters.VIDEO, handle_media))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
