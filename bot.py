from telegram.ext import ApplicationBuilder

from config import TOKEN

# Import handlers
from handlers.start import start_handler
from handlers.stories import stories_handler
from handlers.admin import admin_handler
from handlers.reactions import reaction_handler
from handlers.comments import comment_handler
from handlers.profile import profile_handler


def main():
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

    # Start listening for updates
    app.run_polling()


if __name__ == "__main__":
    main()
