import telebot
from telebot import types
import messages

bot = telebot.TeleBot(messages.token)
bot.set_webhook()

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
            lang = types.KeyboardButton(messages.lang[f'lang_{user_language}'])
            markup.add(grodno)
            markup.add(lang)
            bot.send_message(message.chat.id, "City:", reply_markup=markup)
        elif message.text == 'ru':
            user_language = 'ru'
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            grodno = types.KeyboardButton(messages.city[f'city_{user_language}'])
            lang = types.KeyboardButton(messages.lang[f'lang_{user_language}'])
            markup.add(grodno)
            markup.add(lang)
            bot.send_message(message.chat.id, "Город:", reply_markup=markup)
        if message.text == messages.lang[f'lang_{user_language}']:
            start(message)
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
            back = types.KeyboardButton(messages.back[f'back_{user_language}'])
            markup.add(yanka, agrarian, medical)
            markup.add(back,menu)
            bot.send_message(message.chat.id, "Choose what you want to find ", reply_markup=markup)
        elif message.text == messages.menu[f'menu_{user_language}']:
            message.chat.type = 'private'
            message.text = user_language
            bot_message(message)
            #start(message)
        elif message.text == messages.back[f'back_{user_language}']:
            message.chat.type = 'private'
            message.text = messages.city[f'city_{user_language}']
            bot_message(message)
            #start(message)
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
            old = types.KeyboardButton(messages.old[f'old_{user_language}'])
            new = types.KeyboardButton(messages.new[f'new_{user_language}'])
            chu = types.KeyboardButton(messages.chu[f'chu_{user_language}'])
            jil = types.KeyboardButton(messages.jil[f'jil_{user_language}'])
            sov = types.KeyboardButton(messages.sov[f'sov_{user_language}'])
            menu = types.KeyboardButton(messages.menu[f'menu_{user_language}'])
            back = types.KeyboardButton(messages.back[f'back_{user_language}'])
            markup.add(xav)
            markup.add(old)
            markup.add(new)
            markup.add(chu)
            markup.add(jil)
            markup.add(sov)
            markup.add(back,menu)
            bot.send_message(message.chat.id, "Choose what you want to find ", reply_markup=markup)
        elif message.text == messages.xav[f'xav_{user_language}']:
            bot.send_message(message.chat.id, messages.xavtxt[f'xavtxt_{user_language}'], parse_mode='html')
            bot.send_photo(message.chat.id, 'https://planetabelarus.by/upload/resize_cache/iblock/3d1/1330_887_18e21fe612b4afb807a26ecc22279a1d9/3d1f89091281efe1e6a55425c2a64735.jpg')
        elif message.text == messages.old[f'old_{user_language}']:
            bot.send_message(message.chat.id, messages.oldtxt[f'oldtxt_{user_language}'], parse_mode='html')
            bot.send_photo(message.chat.id, 'https://upload.wikimedia.org/wikipedia/commons/7/79/Horadnia_%28Hrodna%29%2C_Stary_zamak._%D0%93%D0%BE%D1%80%D0%B0%D0%B4%D0%BD%D1%8F%2C_%D0%A1%D1%82%D0%B0%D1%80%D1%8B_%D0%B7%D0%B0%D0%BC%D0%B0%D0%BA_%282021%29_03.jpg')
        elif message.text == messages.new[f'new_{user_language}']:
            bot.send_message(message.chat.id, messages.newtxt[f'newtxt_{user_language}'], parse_mode='html')
            bot.send_photo(message.chat.id, 'https://ekskursii.by/images/obj2/16258/14_.jpg')
        elif message.text == messages.jil[f'jil_{user_language}']:
            bot.send_message(message.chat.id, messages.jiltxt[f'jiltxt_{user_language}'], parse_mode='html')
            bot.send_photo(message.chat.id, 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/%D0%9F%D0%B0%D1%80%D0%BA_%D0%96%D0%B8%D0%BB%D0%B8%D0%B1%D0%B5%D1%80%D0%B0_1.JPG/1200px-%D0%9F%D0%B0%D1%80%D0%BA_%D0%96%D0%B8%D0%BB%D0%B8%D0%B1%D0%B5%D1%80%D0%B0_1.JPG')
        elif message.text == messages.chu[f'chu_{user_language}']:
            bot.send_message(message.chat.id, messages.chutxt[f'chutxt_{user_language}'], parse_mode='html')
            bot.send_photo(message.chat.id, 'https://traveling.by/files/houses/2020/06/bf349f5c60f022c5035e2c78d2802717-thumb-642x427.jpg')
        elif message.text == messages.sov[f'sov_{user_language}']:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(messages.sov[f'sov_{user_language}'], url="https://theculturetrip.com/europe/belarus/articles/the-best-things-to-see-and-do-in-grodno-belarus/"))
            bot.send_message(message.chat.id, messages.sov[f'sovtxt_{user_language}'], parse_mode='html')
            bot.send_message(message.chat.id, "More info:", reply_markup=markup)
            bot.send_photo(message.chat.id, 'https://fs.tonkosti.ru/el/mu/elmuhavkoj4sg0kkogw40ogww.jpg')
        elif message.text == messages.ent[f'ent_{user_language}']:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(messages.mus[f'mus_{user_language}'], url="https://www.tripadvisor.com/Attractions-g661665-Activities-c49-Grodno_Grodno_Region.html"))
            markup.add(types.InlineKeyboardButton(messages.the[f'the_{user_language}'], url="https://www.tripadvisor.com/Attractions-g661665-Activities-c58-t116-Grodno_Grodno_Region.html"))
            markup.add(types.InlineKeyboardButton(messages.club[f'club_{user_language}'], url="https://www.tripadvisor.com/Attractions-g661665-Activities-c20-t99-Grodno_Grodno_Region.html"))
            markup.add(types.InlineKeyboardButton(messages.pool[f'pool_{user_language}'], url="https://grodno.in/pool/"))
            markup.add(types.InlineKeyboardButton(messages.shop[f'shop_{user_language}'], url="https://www.tripadvisor.com/Attractions-g661665-Activities-c26-Grodno_Grodno_Region.html"))
            bot.send_message(message.chat.id, "Choose what you want to find", reply_markup=markup)
        elif message.text == messages.cat[f'cat_{user_language}']:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(messages.deli[f'deli_{user_language}'], url="https://gr.ayle.ru/dostavka-edy-v-grodno/"))
            markup.add(types.InlineKeyboardButton(messages.cafe[f'cafe_{user_language}'], url="https://gr.ayle.ru/kafe-v-grodno/"))
            markup.add(types.InlineKeyboardButton(messages.piz[f'piz_{user_language}'], url="https://gr.ayle.ru/pizzerii-v-grodno/"))
            markup.add(types.InlineKeyboardButton(messages.rest[f'rest_{user_language}'], url="https://gr.ayle.ru/restorany-v-grodno/"))
            markup.add(types.InlineKeyboardButton(messages.fast[f'fast_{user_language}'], url="https://gr.ayle.ru/bystroe-pitanie-v-grodno/"))
            markup.add(types.InlineKeyboardButton(messages.cant[f'cant_{user_language}'], url="https://gr.ayle.ru/stolovye-v-grodno/"))
            markup.add(types.InlineKeyboardButton(messages.sush[f'sush_{user_language}'], url="https://gr.ayle.ru/sushi-bary-v-grodno/"))
            bot.send_message(message.chat.id, messages.choice[f'choice_{user_language}'], reply_markup=markup)
@bot.message_handler(commands=['info'])
def info(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Universities", url = "https://www.tripadvisor.com/Attractions-g661665-Activities-c49-Grodno_Grodno_Region.html"))
    markup.add(types.InlineKeyboardButton("Historical sights", url="https://www.tripadvisor.com/Attractions-g661665-Activities-c58-t116-Grodno_Grodno_Region.html"))
    markup.add(types.InlineKeyboardButton("Entertainment", url="https://www.tripadvisor.com/Attractions-g661665-Activities-c20-t99-Grodno_Grodno_Region.html"))
    markup.add(types.InlineKeyboardButton("Catering establishments", url="https://grodno.in/pool/"))
    bot.send_message(message.chat.id,"Choose what you want to find", reply_markup=markup)



bot.polling(none_stop=True)