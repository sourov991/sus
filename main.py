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
                bot.send_message(chat_id=message.chat.id, text=message_text, parse_mode='HTML')

# Start the bot
bot.polling()
