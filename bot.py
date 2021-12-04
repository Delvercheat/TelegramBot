import telebot
import config

TOKEN = '5063370371:AAHdjKX1dBrAB_xdfLP4SzxP_Fi3hoqvFxs' #bot token
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['about'])
def about(message):
    
    bot.send_message(message.chat.id, "Мой разработчик: @pycharmist(больше инфы пока не добавил).".format(message.from_user, bot.get_me()))


@bot.message_handler(commands=['start'])
def welcome(message):

    bot.send_message(message.chat.id, "Добро пожаловать! Я - тестовый бот PyBot созданный Pycharmistом. Пока что я только повторяю ваши сообщения но мой создатель уже работает над чем то класным. кстати из нового уже доступка команда /about".format(message.from_user, bot.get_me()))


@bot.message_handler(content_types=['text'])
def say(message):
    
    bot.send_message(message.chat.id, message.text)


bot.polling(non_stop=True)