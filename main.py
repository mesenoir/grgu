import telebot
from telebot import types

bot = telebot.TeleBot('5797094599:AAHTLShhcZ-Xn1OH0JBLdXYQcyah92G4W1g')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mess = f"Hello, {message.from_user.first_name} {message.from_user.last_name}"
    grodno = types.KeyboardButton('Grodno')
    markup.add(grodno)
    bot.send_message(message.chat.id, mess, reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Grodno':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            uni = types.KeyboardButton('Universities')
            hsights = types.KeyboardButton('Historical sights')
            enter = types.KeyboardButton('Entertainment')
            catering = types.KeyboardButton('Catering establishments')
            menu = types.KeyboardButton('Main Menu')
            markup.add(uni,hsights,enter,catering,menu)
            bot.send_message(message.chat.id, "Choose what you want to find ", reply_markup=markup)
        elif message.text == 'Universities':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            yanka = types.KeyboardButton('Yanka Kupala Grodno State University')
            agrarian = types.KeyboardButton('Grodno Agrarian University')
            medical = types.KeyboardButton('Grodno State Medical University')
            menu = types.KeyboardButton('Main Menu')
            markup.add(yanka, agrarian, medical, menu)
            bot.send_message(message.chat.id, "Choose what you want to find ", reply_markup=markup)
        elif message.text == "Main Menu":
            start(message)



@bot.message_handler(commands=['info'])
def info(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Universities", url = "https://climate.nasa.gov/"))
    markup.add(types.InlineKeyboardButton("Historical sights", url="https://climate.nasa.gov/"))
    markup.add(types.InlineKeyboardButton("Entertainment", url="https://climate.nasa.gov/"))
    markup.add(types.InlineKeyboardButton("Catering establishments", url="https://climate.nasa.gov/"))
    bot.send_message(message.chat.id,"Choose what you want to find", reply_markup=markup)



bot.polling(none_stop=True)