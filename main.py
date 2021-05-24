import os

import telegram
from telegram.ext import Updater, CommandHandler

updater = Updater(token=os.environ['TG_BOT_KEY'])
dispatcher = updater.dispatcher


def start(update, context):
    """
    Welcome the user to the bot
    """
    welcome_message = "👋 Welcome to your AWS Basic course!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message,
                             parse_mode=telegram.ParseMode.MARKDOWN, disable_web_page_preview=True)


def greet(update, context):
    """
    Show users' data

    :param update:
    :param context:
    :return:
    """
    start(update, context)


start_handler = CommandHandler('start', start)
greets_handles = CommandHandler('greet', greet)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(greets_handles)

updater.start_polling()
