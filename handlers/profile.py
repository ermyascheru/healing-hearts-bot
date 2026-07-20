from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from utils.database import load_users



async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):

    users = load_users()

    user_id = update.effective_user.id


    for user in users:

        if user["id"] == user_id:

            await update.message.reply_text(
                "🌱 Your Healing Profile\n\n"
                f"Stories shared: {user['stories_shared']}\n"
                f"Comments: {user['comments_sent']}\n"
                f"Support given: {user['support_given']}"
            )

            return


    await update.message.reply_text(
        "You don't have a profile yet. Use /start first."
    )



profile_handler = CommandHandler(
    "profile",
    profile
)
