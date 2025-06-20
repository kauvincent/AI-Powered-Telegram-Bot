import os
import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Config
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Command: /start
async def start(update: Update, context):
    await update.message.reply_text("Hi! I'm your AI assistant. Ask me anything!")

# Handle messages
async def chat(update: Update, context):
    user_input = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    await update.message.reply_text(response.choices[0].message.content)

# Run bot
if __name__ == "__main__":
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    app.run_polling()
