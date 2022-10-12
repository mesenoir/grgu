import telebot
from telebot import types
import messages

bot = telebot.TeleBot(messages.token)

user_language = " "

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mess = f"Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}"
    #mess = f"{messages.hello_user[f'hello_{user_language}']} {message.from_user.first_name} {message.from_user.last_name}"
    user_language_en = types.KeyboardButton('en')
    user_language_ru = types.KeyboardButton('ru')
    markup.add(user_language_en, user_language_ru)
    bot.send_message(message.chat.id, f"{mess} \nChoose your language:\nВыберите свой язык: ", reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def bot_message(message):
    global user_language
    if message.chat.type == 'private':
        if message.text == 'en':
            user_language = 'en'
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            grodno = types.KeyboardButton(messages.city[f'city_{user_language}'])
            markup.add(grodno)
            bot.send_message(message.chat.id, "City:", reply_markup=markup)
        elif message.text == 'ru':
            user_language = 'ru'
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            grodno = types.KeyboardButton(messages.city[f'city_{user_language}'])
            markup.add(grodno)
            bot.send_message(message.chat.id, "Город:", reply_markup=markup)
        if message.text == messages.city[f'city_{user_language}']:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            uni = types.KeyboardButton(messages.uni[f'uni_{user_language}'])
            hsights = types.KeyboardButton(messages.hsights[f'hsights_{user_language}'])
            enter = types.KeyboardButton(messages.ent[f'ent_{user_language}'])
            catering = types.KeyboardButton(messages.cat[f'cat_{user_language}'])
            menu = types.KeyboardButton(messages.menu[f'menu_{user_language}'])
            markup.add(uni,hsights,enter,catering)
            markup.add(menu)
            bot.send_message(message.chat.id, "Choose what you want to find ", reply_markup=markup)
        elif message.text == messages.uni[f'uni_{user_language}']:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            yanka = types.KeyboardButton(messages.yanka[f'yanka_{user_language}'])
            agrarian = types.KeyboardButton(messages.agrar[f'agrar_{user_language}'])
            medical = types.KeyboardButton(messages.med[f'med_{user_language}'])
            menu = types.KeyboardButton(messages.menu[f'menu_{user_language}'])
            markup.add(yanka, agrarian, medical)
            markup.add(menu)
            bot.send_message(message.chat.id, "Choose what you want to find ", reply_markup=markup)
        elif message.text == messages.menu[f'menu_{user_language}']:
            start(message)
        elif message.text == messages.yanka[f'yanka_{user_language}']:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(messages.pre[f'pre_{user_language}'], url="http://fdp.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.math[f'math_{user_language}'], url="http://mf.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.eng[f'eng_{user_language}'], url="https://fbt.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.tur[f'tur_{user_language}'], url="https://fh.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.psy[f'psy_{user_language}'], url="https://psf.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.law[f'law_{user_language}'], url="https://lf.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.phy[f'phy_{user_language}'], url="https://ftf.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.mach[f'mach_{user_language}'], url="http://fit.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.phis[f'phis_{user_language}'], url="http://ffc.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.eco[f'eco_{user_language}'], url="http://fem.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.phil[f'phil_{user_language}'], url="http://phf.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.mil[f'mil_{user_language}'], url="http://mil.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.bio[f'bio_{user_language}'], url="http://fbe.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.art[f'art_{user_language}'], url="http://art.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.bib[f'bib_{user_language}'], url="http://lib.grsu.by/"))
            markup.add(types.InlineKeyboardButton(messages.ped[f'ped_{user_language}'], url="http://fp.grsu.by/"))
            bot.send_message(message.chat.id, "Choose what you want to find", reply_markup=markup)
        elif message.text == messages.agrar[f'agrar_{user_language}']:
            bot.send_message(message.chat.id, messages.info[f'info_{user_language}'], parse_mode='html')
        elif message.text == messages.med[f'med_{user_language}']:
            bot.send_message(message.chat.id, messages.info[f'info_{user_language}'], parse_mode='html')
        elif message.text == messages.hsights[f'hsights_{user_language}']:
            bot.send_message(message.chat.id, messages.grodno[f'grodno_{user_language}'], parse_mode='html')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            xav = types.KeyboardButton(messages.xav[f'xav_{user_language}'])
            menu = types.KeyboardButton(messages.menu[f'menu_{user_language}'])
            markup.add(xav)
            markup.add(menu)
            bot.send_message(message.chat.id, "Choose what you want to find ", reply_markup=markup)
        elif message.text == messages.xav[f'xav_{user_language}']:
            bot.send_message(message.chat.id, messages.xavtxt[f'xavtxt_{user_language}'], parse_mode='html')
            bot.send_photo(message.chat.id, 'https://planetabelarus.by/upload/resize_cache/iblock/3d1/1330_887_18e21fe612b4afb807a26ecc22279a1d9/3d1f89091281efe1e6a55425c2a64735.jpg')

@bot.message_handler(commands=['info'])
def info(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Universities", url = "https://climate.nasa.gov/"))
    markup.add(types.InlineKeyboardButton("Historical sights", url="https://climate.nasa.gov/"))
    markup.add(types.InlineKeyboardButton("Entertainment", url="https://climate.nasa.gov/"))
    markup.add(types.InlineKeyboardButton("Catering establishments", url="https://climate.nasa.gov/"))
    bot.send_message(message.chat.id,"Choose what you want to find", reply_markup=markup)



bot.polling(none_stop=True)