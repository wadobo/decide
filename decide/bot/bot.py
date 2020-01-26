from telegram.ext import Updater, CommandHandler

import telegram



def prueba1(update, context):
    update.message.reply_text('Hola {}'.format(update.message.from_user.first_name))

def prueba2(update, context):
    update.message.reply_text('prueba2')

def prueba3(update, context):
    update.message.reply_text('prueba3')

def prueba4(update, context):
    update.message.reply_text('prueba4')

def prueba5(update, context):
    update.message.reply_text('prueba5')

def main():
    bot = telegram.bot.Bot(token='939132779:AAH_1-kNBHGx_tOZxMtF8JjmdixHEaDLpLw')
    updater = Updater('939132779:AAH_1-kNBHGx_tOZxMtF8JjmdixHEaDLpLw', use_context=True)

    updater.dispatcher.add_handler(CommandHandler('prueba1', prueba1))
    updater.dispatcher.add_handler(CommandHandler('prueba2', prueba2))
    updater.dispatcher.add_handler(CommandHandler('prueba3', prueba3))
    updater.dispatcher.add_handler(CommandHandler('prueba4', prueba4))
    updater.dispatcher.add_handler(CommandHandler('prueba5', prueba5))

    updater.start_polling()
    updater.idle()
   
   
   
 
   
   
if __name__ == '__main__':
    main() 