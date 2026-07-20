from telegram import Update
from telegram.ext import (
    ContextTypes,
    CommandHandler
)


async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "❤️ Your feelings are valid.\n\n"
        "Healing takes time. Keep moving forward "
        "one day at a time. 🌱"
    )


support_handler = CommandHandler(
    "support",
    support
)
