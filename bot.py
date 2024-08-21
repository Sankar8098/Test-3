from telegram.ext import Updater, MessageHandler, Filters
from config.config import BOT_TOKEN, LOG_CHANNEL_ID

# Function to log forwarded messages
def log_forwarded_message(update, context):
    message = update.message
    
    if message.forward_from_chat:
        forward_from_channel = message.forward_from_chat.title
        forward_date = message.forward_date

        forward_user = message.from_user.username or message.from_user.full_name
        forward_user_id = message.from_user.id

        log_message = (f"Video forwarded from channel '{forward_from_channel}'\n"
                       f"Forwarded by: {forward_user} (ID: {forward_user_id})\n"
                       f"Forwarded at: {forward_date}")
        
        # Log the message in your log channel
        context.bot.send_message(chat_id=LOG_CHANNEL_ID, text=log_message)

# Main function to set up the bot and handlers
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handle forwarded messages
    dp.add_handler(MessageHandler(Filters.forwarded & Filters.video, log_forwarded_message))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
