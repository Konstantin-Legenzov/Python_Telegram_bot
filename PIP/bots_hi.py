from telegram.ext import Updater, CommandHandler, Update, CallbackContext
from telegram import Update
from constants import TOKEN
from anecAPI import anecAPI




def get_joke(update: Update, context: CallbackContext):
    after_command = context.args
    update.message.reply_text(anecAPI.modern_joke())
    print(after_command)

updater = Updater(TOKEN)
dispetcher = updater.dispatcher

joke_handler = CommandHandler('joke', get_joke)

dispetcher.add_handler(joke_handler)

print('server start')
updater.start_polling()
updater.idle()

