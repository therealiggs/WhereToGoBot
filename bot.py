import telebot
from telebot.types import Message
from telebot import apihelper


token = '776536658:AAHuHAi28nhFCKyGgASAHWd-063hyItVEmQ'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.send_message(message.chat.id, 'No description yet...')


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def text_handler(message: Message):
    if 'привет' in message.text.lower():
        bot.send_message(message.chat.id, 'Тебе тоже привет!')
    else:
        bot.send_message(message.chat.id, 'Прости, я тебя не понимаю')


bot.polling(timeout=60)


