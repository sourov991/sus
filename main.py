import os
import requests
import telebot

bot = telebot.TeleBot('5505853286:AAHyqoQPNoZzwyP0-Ws11t74GFxseEKNnX4')

@bot.message_handler(func=lambda message: True)
def process_message(message):
    # Check if the message contains a link
    if message.entities is not None:
        for entity in message.entities:
            if entity.type == 'url':
                # Extract the link from the message
                link = message.text[entity.offset:entity.offset + entity.length]

                # Replace '#' with '@' in the link
                link = link.replace('#', '@')

                # Add a prefix to the link
                prefix = 'https://spamx.id/stripe/?cspk='
                link = prefix + link

                # Retrieve the response from the prefixed link
                response = requests.get(link)

                # Parse the JSON response
                data = response.json()

                # Extract relevant information from the JSON object
                amount_due = data['amount_due']
                name = data['name']
                session_id = data['session_id']
                pk = data['pk']
                email = data.get('email', 'N/A')

                # Format the message to send to the user
                message_text = f"<code>Payment page details:</code>\n\n" \
                               f"<code>Amount due:</code> {amount_due}\n\n" \
                               f"<code>Name:</code> {name}\n\n" \
                               f"<code>Session ID:</code> {session_id}\n\n" \
                               f"<code>PK:</code> {pk}\n\n" \
                               f"<code>Email:</code> {email}"

                # Send the message to the user with monospace format
                bot.send_message(chat_id=message.chat.id, text=message_text, parse_mode='HTML')import os

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

# Start the bot
bot.polling()
