from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler

from utils.reaction_database import (
    add_reaction,
    count_reactions
)



async def reaction_button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()


    story_id = query.data.split(":")[1]


    added = add_reaction(
        story_id,
        update.effective_user.id
    )


    count = count_reactions(story_id)


    if added:

        await query.answer(
            "❤️ Support added!",
            show_alert=True
        )


    else:

        await query.answer(
            "You already supported this story ❤️",
            show_alert=True
        )


    await query.edit_message_reply_markup(
        reply_markup=query.message.reply_markup
    )



reaction_handler = CallbackQueryHandler(
    reaction_button,
    pattern="support:"
)
