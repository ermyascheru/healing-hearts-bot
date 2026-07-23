import os
import threading

from flask import Flask
from telegram.ext import ApplicationBuilder

from config import TOKEN

# Import handlers
from handlers.start import start_handler
from handlers.stories import stories_handler
from handlers.admin import admin_handler
from handlers.reactions import reaction_handler
from handlers.comments import comment_handler
from handlers.profile import profile_handler


# -----------------------------
# Flask server for Render
# -----------------------------

web_app = Flask(__name__)


@web_app.route("/")
def home():
    return "❤️ Healing Hearts Bot is running!"


def run_web():
    port = int(os.environ.get("PORT", 10000))

    web_app.run(
        host="0.0.0.0",
        port=port
    )


# -----------------------------
# Telegram Bot
# -----------------------------

def run_bot():

    if not TOKEN:
        print("❌ TOKEN is missing from environment variables")
        return

    print("🔑 Token loaded")

    app = ApplicationBuilder().token(TOKEN).build()

    # Register handlers
    app.add_handler(start_handler)
    app.add_handler(stories_handler)
    app.add_handler(admin_handler)
    app.add_handler(reaction_handler)
    app.add_handler(comment_handler)
    app.add_handler(profile_handler)

    print("❤️ Healing Hearts Bot started!")

    # Start Telegram polling
    app.run_polling(
        drop_pending_updates=True
    )


# -----------------------------
# Start everything
# -----------------------------

def main():

    # Start Flask for Render
    flask_thread = threading.Thread(
        target=run_web,
        daemon=True
    )

    flask_thread.start()

    # Start Telegram bot
    run_bot()


if __name__ == "__main__":
    main()
