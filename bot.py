import telebot
from telebot.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


token = '776536658:AAHuHAi28nhFCKyGgASAHWd-063hyItVEmQ'
bot = telebot.TeleBot(token)
city = 'Not set'


@bot.message_handler(commands=['help'])
def command_handler(message: Message):
    bot.send_message(message.chat.id, 'No description yet...')


@bot.message_handler(commands=['start'])
def command_handler(message: Message):
    keyboard = InlineKeyboardMarkup()
    button_moscow = InlineKeyboardButton(text='В Москве', callback_data="set_city_moscow")
    button_swamp = InlineKeyboardButton(text='В Санкт-Петербурге', callback_data="set_city_swamp")
    keyboard.add(button_moscow, button_swamp)
    bot.send_message(message.chat.id, text='Выберите, где собираетесь'
                                           ' чиллить и флексить, и я отведу'
                                           ' Вас в подходящее местечко:',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data.startswith('set_city_'):
        global city
        bot.send_message(chat_id=call.message.chat.id,
                         text='Город успешно выбран!')
        if call.data == 'set_city_moscow':
            city = 'moscow'
        else:
            city = 'swamp'
        print(city)

    # elif call.inline_message_id:
    #    if call.data == "test":
    #       bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def text_handler(message: Message):
    if 'привет' in message.text.lower():
        bot.send_message(message.chat.id, 'Тебе тоже привет!')
    else:
        bot.send_message(message.chat.id, 'Прости, я тебя не понимаю')


bot.polling(timeout=60)


