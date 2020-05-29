from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

def start(bot,update):
    update.message.reply_text("I'm a bot, Nice to meet you!")

def convert_to_uppercase(bot,update):
    update.message.reply_text(update.message.text.upper())

def main():
    #Reading the token from API_Token.txt file
    try:
        token_file=open(r'API_Token.txt','r')
        TOKEN=token_file.read()
    except:
        print("Error in reading API Token")
        exit()

    #Creating Updater object which will get the Telegram updates
    updater=Updater(token=TOKEN)

    #Linking updater to dispatcher which has appropriate event handlers method attached to it
    dispatcher=updater.dispatcher
    print("Bot started") 
     
    #Creating a CommandHandler Object to link command to function and adding it to dispatcher
    start_handler=CommandHandler('start',start)
    dispatcher.add_handler(start_handler)

    #Creating a MessageHandler Object to link non-command messages to function
    uppercase_handler=MessageHandler(Filters.text,convert_to_uppercase)
    dispatcher.add_handler(uppercase_handler)

    #Start the bot
    updater.start_polling()

    #Run the bot until the developer presses Ctrl-C
    updater.idle()

if __name__=="__main__":
    main()