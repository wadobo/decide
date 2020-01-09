from telegram.ext import Updater, CommandHandler

import telegram



def prueba1(update, context):
    update.message.reply_text('Hola {}'.format(update.message.from_user.first_name))

def prueba2(update, context):
    update.message.reply_text('prueba2')


def main():
    bot = telegram.bot.Bot(token='939132779:AAH_1-kNBHGx_tOZxMtF8JjmdixHEaDLpLw')
    updater = Updater('939132779:AAH_1-kNBHGx_tOZxMtF8JjmdixHEaDLpLw', use_context=True)

    bot.send_message(chat_id='@decidezapdos', text="Este es un mensaje de prueba para el canal @decidezapdos")
    updater.dispatcher.add_handler(CommandHandler('prueba1', prueba1))
    updater.dispatcher.add_handler(CommandHandler('prueba2', prueba2))

    updater.start_polling()
    updater.idle()
   
   
   
 
   
   
if __name__ == '__main__':
    main() 