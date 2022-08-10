import telebot
from telebot import types
bot = telebot.TeleBot('5445682897:AAEmQTgZjTGgwiKN0wujqtak7LaUGvvoWM4')

@bot.message_handler(commands=['start'])
def start(message):
    mass = f'Assalomu Alaykum, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mass, parse_mode='html' )

#@bot.message_handler(content_types=['text'])
#def get_user_text(message):
#    if message.text == "Salom":
#       bot.send_message(message.chat.id, "Assalomu Alaykum", parse_mode='html')
#    elif message.text == "id":
#        bot.send_message(message.chat.id, f"Bu sizni idingiz: {message.from_user.id} ", parse_mode='html')
#    elif message.text == "photo":
#        photo = open('photo_22.jpg', 'rb')
#        bot.send_photo(message.chat.id, photo)
#    else:
#        bot.send_message(message.chat.id, "Men sizni tushunmadim", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Ooo daxshat rasmku :)", parse_mode='html')

@bot.message_handler(commands=["website"])
def website(massage):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Bizning saytga tashrif buyirish', url="https://t.me/this_my_perfect_life"))
    bot.send_message(massage.chat.id, 'Saytimizga kiring', reply_markup=markup)

@bot.message_handler(commands=["help"])
def website(massage):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')
    markup.add(website, start)
    bot.send_message(massage.chat.id, 'Saytimizga kiring', reply_markup=markup)


bot.polling(none_stop=True)