from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from utils.database import add_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    add_user(
        update.effective_user.id,
        update.effective_user.username,
        update.effective_user.first_name
    )

    await update.message.reply_text(
        "❤️ Welcome to Healing Hearts Ethiopia 🇪🇹"
    )


start_handler = CommandHandler(
    "start",
    start
)
