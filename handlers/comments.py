from telegram import Update
from telegram.ext import (
    ContextTypes,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    filters
)

from utils.comment_database import create_comment


WAITING_COMMENT = 1



async def start_comment(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()


    story_id = query.data.split(":")[1]


    context.user_data["comment_story"] = story_id


    await context.bot.send_message(
        chat_id=query.from_user.id,
        text=(
            "💬 Write your supportive message.\n\n"
            "Remember to be kind ❤️"
        )
    )


    return WAITING_COMMENT



async def receive_comment(update: Update, context: ContextTypes.DEFAULT_TYPE):

    story_id = context.user_data["comment_story"]

    create_comment(
        story_id,
        update.effective_user.id,
        update.message.text
    )


    await update.message.reply_text(
        "✅ Your comment was submitted for review ❤️"
    )


    return ConversationHandler.END



comment_handler = ConversationHandler(

    entry_points=[
        CallbackQueryHandler(
            start_comment,
            pattern="comment:"
        )
    ],

    states={

        WAITING_COMMENT: [

            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                receive_comment
            )

        ]

    },

    fallbacks=[]
)
