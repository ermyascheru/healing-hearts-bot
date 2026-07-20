from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    ContextTypes,
    CallbackQueryHandler
)

from config import ADMIN_ID, CHANNEL_USERNAME

from utils.story_database import get_story_by_id



async def send_to_admin(context, story_id, story_text):

    keyboard = [
        [
            InlineKeyboardButton(
                "✅ Approve",
                callback_data=f"approve:{story_id}"
            ),

            InlineKeyboardButton(
                "❌ Reject",
                callback_data=f"reject:{story_id}"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)


    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            "📩 New Story Submission\n\n"
            f"{story_text}\n\n"
            f"Story ID: {story_id}"
        ),
        reply_markup=reply_markup
    )



async def admin_action(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()


    action, story_id = query.data.split(":", 1)


    story = get_story_by_id(story_id)


    if story is None:

        await query.edit_message_text(
            "❌ Story not found."
        )

        return



    if action == "approve":

        keyboard = [
            [
                InlineKeyboardButton(
                    "❤️ Support",
                    callback_data=f"support:{story_id}"
                ),

                InlineKeyboardButton(
                    "💬 Comment",
                    callback_data=f"comment:{story_id}"
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)


        await context.bot.send_message(
            chat_id=CHANNEL_USERNAME,
            text=(
                "❤️ Anonymous Story\n\n"
                f"🌱 {story['anonymous_name']}\n\n"
                f"{story['text']}\n\n"
                "— Healing Hearts Ethiopia 🇪🇹"
            ),
            reply_markup=reply_markup
        )


        await query.edit_message_text(
            "✅ Story approved and posted."
        )


    elif action == "reject":

        await query.edit_message_text(
            "❌ Story rejected."
        )



admin_handler = CallbackQueryHandler(
    admin_action
)
