import os
from flask import Flask, request
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
)

from config import TOKEN

from handlers.start import start_handler
from handlers.stories import stories_handler
from handlers.admin import admin_handler
from handlers.reactions import reaction_handler
from handlers.comments import comment_handler
from handlers.profile import profile_handler


app = Flask(__name__)

telegram_app = (
    ApplicationBuilder()
    .token(TOKEN)
    .build()
)


# Register handlers
telegram_app.add_handler(start_handler)
telegram_app.add_handler(stories_handler)
telegram_app.add_handler(admin_handler)
telegram_app.add_handler(reaction_handler)
telegram_app.add_handler(comment_handler)
telegram_app.add_handler(profile_handler)


@app.route("/")
def home():
    return "❤️ Healing Hearts Bot is running!"


@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    update = Update.de_json(
        request.get_json(force=True),
        telegram_app.bot
    )

    await telegram_app.process_update(update)

    return "ok"


@app.before_request
async def startup():
    if not telegram_app.running:
        await telegram_app.initialize()
        await telegram_app.start()

        webhook_url = (
            f"{os.environ.get('RENDER_EXTERNAL_URL')}/{TOKEN}"
        )

        await telegram_app.bot.set_webhook(webhook_url)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port
    )
