from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot_rand.log')

import random
secure_random = random.SystemRandom()
#def greet_user(bot, update):
 #   print('Вызван /start')
  #  print(update)
list=[]

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)
    list


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    list.append(user_text)
    update.message.reply_text(secure_random.choice(list))



def main():
    mybot=Updater("698357850:AAGw6kPTBLXQT8_OF3oHusyLBFP4WNWJumc", request_kwargs=PROXY)


    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()