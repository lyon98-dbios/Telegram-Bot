
#Fetching the Libraries
from telegram import *
from telegram.ext import *


#Fetching the bot information
bot = Bot("Past token ID")
print(bot.get_me())


#Update for future changes
updater=Updater("Past token ID ",use_context=True)
#use_context : if your telegram version is low then use false else use true

#A dispatcher is used to dispatch this update to our telegram bot
dispatcher=updater.dispatcher


# We create the command for a specific reply that we want
def test_fnc2(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welcome to the world of Otakus ",
        )
start_value2=CommandHandler('start', test_fnc2)
dispatcher.add_handler (start_value2)

#adding more Commands
def test_fnc(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="github link: https://github.com/lyon98-dbios/ ",
        )
start_value=CommandHandler('python', test_fnc)
dispatcher.add_handler (start_value)

#Polling The Update
updater.start_polling()
