########################################################
#                        SassineBot                 #
#                       version 0.0                    #
#                       williamjallot                      #
########################################################
import os
import logging
import requests
import random
import os
import re

from  methods import li7wak, ilost, joke, midNight,goodDog,quotes, nasaPicture, help, recommandation

# for now()
import datetime
import telegram

# for timezone()
import pytz
import variables
import importlib.util
import datetime
importlib.util.spec_from_file_location("/home/LordofSquid/.local/lib/python3.6/site-packages/pyjokes")
import pyjokes

from numpy import random as rn
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from subprocess import CalledProcessError

TOKEN = os.getenv('TOKEN')


variables.bot = telegram.Bot(token=TOKEN)
updates = variables.bot.getUpdates()

updater = telegram.ext.Updater(bot=variables.bot)

#variables.bot.send_message(chat_id=kachowId, text='Hello, group! My name is Marwa')
#variables.bot.send_poll(chat_id = kachowId, question="Life",options = ["maybe", "idk", "None","COOKIE","TCP"], is_anonymous = False, type = telegram.Poll.REGULAR)

#updater = Updater(TOKEN, use_context=True)


updater.dispatcher.add_handler(MessageHandler(Filters.text, li7wak))
updater.dispatcher.add_handler(MessageHandler(Filters.text, ilost),group=1)
updater.dispatcher.add_handler(MessageHandler(Filters.text, joke),group=2)
updater.dispatcher.add_handler(MessageHandler(Filters.text, midNight),group=3)
updater.dispatcher.add_handler(MessageHandler(Filters.text, goodDog),group=4)
updater.dispatcher.add_handler(MessageHandler(Filters.text, nasaPicture),group=6)
updater.dispatcher.add_handler(CommandHandler(["help"], help) ,group=7)
updater.dispatcher.add_handler(CommandHandler(["quote"], quotes) ,group=8)
updater.dispatcher.add_handler(CommandHandler(["recommandation"], recommandation) ,group=9)
updater.start_polling()

print("Your telegram bot is running!")

updater.idle()