from telegram.ext import Updater
from telegram.ext import CommandHandler

def start(bot,update):
    update.message.reply_text("I'm a bot, Nice to meet you!")

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

    #Creating a CommandHandler Object to link command to function and adding it to dispatcher
    start_handler=CommandHandler('start',start)
    dispatcher.add_handler(start_handler)

    #Start the bot
    updater.start_polling()

    #Run the bot until the developer presses Ctrl-C
    updater.idle()

if __name__=="__main__":
    main()