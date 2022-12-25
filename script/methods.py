import os
import logging
import requests
import random
import os
import re
import telegram
# for now()
import datetime

# for timezone()
import pytz
import variables

import datetime

import pyjokes

from quote import quote 

LI7WAK_sent_dictionnary = {}
LI7WAK_received_dictionnary = {}



quoteCounter = 0

ExistingFeatures = ["ilost","li7wak","joke","trivia","time : Korea, Swiss, China, Usa","attack","quote", "nasa"]

def ilost(update,context) :
      #1 chance sur 1001 pour que le bot envoie j'ai perdu
      if(random.randint(0, 1000) == 4):
        update.message.reply_text("/jaiperdu")
def li7wak(update, context) :
  text = update.message.text
  user_name = update.message.from_user.username
  #si la personne a dit li7wak
  if("li7wak" in text.lower()):
    reply_to_message = update.message.reply_to_message

    #si li7wak n'est pas en réponse à un message ne marche pas
    if reply_to_message is None:
        update.message.reply_text('Tu peux pas li7wak dans le vide nullard.e')
        return

    #si li7wak est en réponse à un qui
    if("qui" in reply_to_message.text.lower()) :
      #update le dictionnaire de li7wak
      updateDictionnary(update, user_name)

      update.message.reply_text(f"{user_name} - {LI7WAK_sent_dictionnary[user_name]}:0")


def updateDictionnary(update, user_name) :
  #si la personne a déjà li7waké augmente son li7wak
  if(user_name in LI7WAK_sent_dictionnary) :
    LI7WAK_sent_dictionnary[user_name] = LI7WAK_sent_dictionnary[user_name] + 1

  #si non crée une nouvelle entrée dans le dictionnaire
  else :
    LI7WAK_sent_dictionnary.update({user_name : 1})

def joke(update, context) :
  if("joke" in update.message.text.lower()) :
    update.message.reply_text(pyjokes.get_joke())


def trivia(update, context) :
    if("trivia" in update.message.text.lower()) :
      update.message.reply_text("")

def midNight(update, context) :
    message = update.message.text

    url = "http://worldtimeapi.org/api/"

    if("timekorea" in message.lower()) :
        current_time = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
        update.message.reply_text(f"It's {current_time.strftime('%A')} in Korea and it is {current_time.hour}h : {current_time.minute}mn")
    if("timeus" in message.lower()) :
        current_time = datetime.datetime.now(pytz.timezone('US/Eastern'))
        update.message.reply_text(f"It's {current_time.strftime('%A')} in USA and it is {current_time.hour}h : {current_time.minute}mn")
    if("timechina" in message.lower()) :
        current_time = datetime.datetime.now(pytz.timezone('Asia/Hong_Kong'))
        update.message.reply_text(f"It's {current_time.strftime('%A')} in Hong Kong and it is {current_time.hour}h : {current_time.minute}mn")
    if("timemorocco" in message.lower()) :
        current_time = datetime.datetime.now(pytz.timezone('Africa/Casablanca'))
        update.message.reply_text(f"It's {current_time.strftime('%A')} in Morocco and it is {current_time.hour}h : {current_time.minute}mn")
    if("timeswiss" in message.lower()) :
        current_time = datetime.datetime.now(pytz.timezone('Europe/Zurich'))
        update.message.reply_text(f"It's {current_time.strftime('%A')} at EPFL and it is {current_time.hour}h : {current_time.minute}mn")

def goodDog(update, context) :
  if("attack" in update.message.text.lower()) :
    print("hey1")
    if(update.message.from_user.username == "williamjallot") :
      update.message.reply_photo("https://kultt.fr/wp-content/uploads/2018/09/Kraken-Chocolat-uai-640x360.jpg")
    else :
      update.message.reply_photo("https://as1.ftcdn.net/v2/jpg/02/18/58/42/1000_F_218584276_YIUjqgAUWarKchOiu81orPd4A45ZlMK9.jpg")

def quotes(update, context) :
    
   
    
    chat_id = update.message.chat.id
    print(chat_id)
    quoteCounter = globals().get("quoteCounter")
    es = quote("life")[quoteCounter]
    globals().update({"quoteCounter" : quoteCounter + 1})

    if(globals().get("quoteCounter") >= len(es)) :
       globals().update({"quoteCounter" : 0})
    
    update.message.reply_text(f"{es['author']} {es['book']} : {es['quote']}")
    
def nasaPicture(update, context) :
  url = "https://api.nasa.gov/planetary/apod?api_key=uw2FrZ33412nvkO1vDyJmYMlmH7sOYdTXVgxvqXl"
  time = datetime.datetime.now(pytz.timezone('Europe/Zurich'))
  if(time.hour == 14 and time.minute == 19 and time.second == 0 or "nasa" in update.message.text.lower()) :
    text = requests.get(url).text
    array = text.split(",")
    url = array[-1][7:-3]
    
    # initializing substrings
    sub1 = '"explanation":"'
    sub2 = '","hdurl":'

    # getting index of substrings
    idx1 = text.index(sub1)
    idx2 = text.index(sub2)
    explanation = text[idx1+15:idx2]
    variables.bot.send_photo(update.message.chat.id,url)
    variables.bot.send_message(update.message.chat.id, explanation)
    
def help(update, context) :
  response = ""
  for string in ExistingFeatures :
    response = response + string + "\n"
def recommandation(update, context) :
  command = "recommandation"
  text = update.message.text
  text = text[(len(command)+1) : (len(text))].lstrip(' ')
  if(not(len(text) == 0)):
    variables.bot.send_message(os.getenv('adminId'),f"{update.message.from_user.username} has sent this recommandation : {text}")
  


