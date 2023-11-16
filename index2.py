from telegram import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    Update, 
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove)
from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler, 
    ContextTypes, 
    CallbackQueryHandler, 
    ConversationHandler,
    MessageHandler,
    filters,
    BaseRateLimiter)
import logging
import asyncio

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

async def echo (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    await context.bot.send_message(chat_id=update.effective_user.id, text=msg)
    
def main() -> None:
    app = ApplicationBuilder().token("1925032512:AAGk0jyH2trNcq6MQOCvhV1yBwvft466Q3U").build()

    # Add handler
    app.add_handler(MessageHandler(filters.Text(), echo))

    # Run app
    print("Running right now")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    asyncio.run(main())
