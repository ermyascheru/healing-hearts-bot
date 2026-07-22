from telegram.ext import ApplicationBuilder
from config import TOKEN

from handlers.start import start_handler
from handlers.stories import stories_handler
from handlers.admin import admin_handler
from handlers.reactions import reaction_handler
from handlers.comments import comment_handler
from handlers.profile import profile_handler

from flask import Flask
import threading


# Flask server for Render Web Service
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "❤️ Healing Hearts Bot is running!"


def run_web():
    web_app.run(host="0.0.0.0", port=10000)


def run_bot():
    # Create the bot application
    app = ApplicationBuilder().token(TOKEN).build()

    # Register handlers
    app.add_handler(start_handler)
    app.add_handler(stories_handler)
    app.add_handler(admin_handler)
    app.add_handler(reaction_handler)
    app.add_handler(comment_handler)
    app.add_handler(profile_handler)

    print("❤️ Healing Hearts Bot is running...")

    # Start Telegram polling
    app.run_polling()


def main():
    # Start Flask in background thread
    threading.Thread(target=run_web).start()

    # Start Telegram bot
    run_bot()


if __name__ == "__main__":
    main()
