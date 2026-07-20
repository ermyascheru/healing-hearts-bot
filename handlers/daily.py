from telegram.ext import ContextTypes
from config import CHANNEL_USERNAME


messages = [
    "❤️ Healing takes time. Be patient with yourself.",
    
    "🌱 You can miss someone and still choose to move forward.",
    
    "💙 Every ending carries a lesson. Your story is still being written.",
    
    "✨ The love you gave was meaningful, even if the relationship ended.",
    
    "🙏 Tomorrow can be better than today. Keep going."
]


async def send_daily_message(context: ContextTypes.DEFAULT_TYPE):

    import random

    message = random.choice(messages)

    await context.bot.send_message(
        chat_id=CHANNEL_USERNAME,
        text=message
    )
