import os
import requests

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
PREFIX_URL = os.getenv('PREFIX_URL')

def replace_hashtag_to_at(bot, update):
    message = update.message.text
    replaced_link = message.replace("#", "@")
    url = f"{PREFIX_URL}/{replaced_link}"
    response = requests.get(url).json()

    amount_due = response.get('amount_due')
    name = response.get('name')
    session_id = response.get('session_id')
    pk = response.get('pk')
    email = response.get('email')

    result = f"""
    `Amount Due: {amount_due}`
    `Name: {name}`
    `Session ID: {session_id}`
    `PK: {pk}`
    `Email: {email}`
    """

    bot.send_message(chat_id=update.message.chat_id, text=result, parse_mode='Markdown')

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("replace", replace_hashtag_to_at))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
