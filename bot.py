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
# Flask app (keeps Render happy)
# -----------------------------
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "❤️ Healing Hearts Bot is running!"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host="0.0.0.0", port=port)


# -----------------------------
# Telegram bot
# -----------------------------
def run_bot():
    print("Bot thread started")

    if not TOKEN:
        print("❌ TOKEN is missing")
        return

    print("TOKEN loaded")

    app = ApplicationBuilder().token(TOKEN).build()

    print("Application built")

    print("Starting polling...")
    app.run_polling()

def main():
    flask_thread = threading.Thread(target=run_web, daemon=True)
    flask_thread.start()

    run_bot()


if __name__ == "__main__":
    main()
