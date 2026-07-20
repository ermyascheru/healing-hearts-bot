from telegram import Update

from handlers.admin import send_to_admin
from utils.story_database import create_story
from utils.database import get_anonymous_name

from telegram.ext import (
    ContextTypes,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters
)


# The step where the bot waits for the user's story
WAITING_FOR_STORY = 1


async def story_start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "❤️ Tell me your story.\n\n"
        "Share what you experienced, what you felt, "
        "or what you learned.\n\n"
        "Your story will be reviewed before being shared."
    )

    return WAITING_FOR_STORY



async def receive_story(update: Update, context: ContextTypes.DEFAULT_TYPE):

    story_text = update.message.text

    anonymous_name = get_anonymous_name(
        update.effective_user.id
    )

    story = create_story(
        update.effective_user.id,
        story_text,
        anonymous_name
    )

    await send_to_admin(
        context,
        story["id"],
        story_text
    )

    await update.message.reply_text(
        "✅ Thank you for sharing your story.\n\n"
        "It has been submitted for review ❤️"
    )

    return ConversationHandler.END

    await update.message.reply_text(
        "✅ Thank you for sharing your story.\n\n"
        "It has been submitted for review ❤️"
    )

    return ConversationHandler.END



async def cancel_story(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "❌ Story submission cancelled."
    )

    return ConversationHandler.END



stories_handler = ConversationHandler(

    entry_points=[
        CommandHandler("story", story_start)
    ],

    states={

        WAITING_FOR_STORY: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                receive_story
            )

        ]

    },

    fallbacks=[
        CommandHandler("cancel", cancel_story)
    ]
)
