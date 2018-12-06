import telebot
from telebot.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import os
import time
from weather import Weather, Unit


weather = Weather(unit=Unit.CELSIUS)
forecasts_moscow = weather.lookup_by_location('moscow').forecast
forecasts_swamp = weather.lookup_by_location('petersburg').forecast
# Здесь с помощью weather-api предзагружаем прогноз погоды,
# т.к. библиотека не работает через прокси

os.startfile(os.path.dirname(__file__) + "/Ultrasurf.exe")
# После чего запускаем прокси. fck da Роскомнадзор
time.sleep(15)
token = '776536658:AAHuHAi28nhFCKyGgASAHWd-063hyItVEmQ'
bot = telebot.TeleBot(token)


def activity_ask(message: Message):  # Выбор типа активности, флекс или же чилл
    keyboard = InlineKeyboardMarkup()
    button_flex = InlineKeyboardButton(text='🤩', callback_data='set_activity_flex')
    button_chill = InlineKeyboardButton(text='🤤', callback_data='set_activity_chill')
    keyboard.add(button_flex, button_chill)
    bot.send_message(message.chat.id, text='Флексить или чиллить? Пора определиться!',
                     reply_markup=keyboard)


def city_ask(message: Message):  # Выбор города
    keyboard = InlineKeyboardMarkup()
    button_moscow = InlineKeyboardButton(text='Москва', callback_data="set_city_moscow")
    button_swamp = InlineKeyboardButton(text='Боло.. Ой, в смысле Питер', callback_data="set_city_swamp")
    keyboard.add(button_moscow, button_swamp)
    bot.send_message(message.chat.id, text='Выберите город, и я отведу'
                                           ' Вас в подходящее местечко:',
                     reply_markup=keyboard)


def digest(message: Message):  # Сообщение с дайджестом от kudago.com
    if city == 'swamp':
        bot.send_message(message.chat.id,
                         'Вот свежий дайджест'
                         ' для Вашего города от '
                         'kudago: https://kudago.com/spb/ ')
    elif city == 'moscow':
        bot.send_message(message.chat.id,
                         'Вот свежий дайджест'
                         ' для Вашего города от '
                         'kudago: https://kudago.com/msk/ ')
    else:
        bot.send_message(message.chat.id,
                         'Похоже, вы еще не выбрали город...'
                         ' Начнём прямо сейчас? Жмите: /start')


@bot.message_handler(commands=['help'])  # Ловец команлы help
def command_handler(message: Message):
    bot.send_message(message.chat.id, 'No description yet...')


@bot.message_handler(commands=['start'])  # Ловец команды start
def command_handler(message: Message):
    city_ask(message)


@bot.callback_query_handler(func=lambda call: True)  # Ловец кнопок
def callback_inline(call):
    if call.data.startswith('set_city_'):
        global city, activity
        bot.send_message(chat_id=call.message.chat.id,
                         text='Город успешно выбран!')
        activity_ask(call.message)
        if call.data == 'set_city_moscow':
            city = 'moscow'
        else:
            city = 'swamp'

    elif call.data == 'set_activity_flex':
        bot.send_message(chat_id=call.message.chat.id,
                         text='Значит, сегодня зажигаем!'
                              ' Сейчас подберу что-нибудь'
                              ' подходящее.')
        activity = 'flex'

    elif call.data == 'set_activity_chill':
        bot.send_message(chat_id=call.message.chat.id,
                         text='Время как следует отдохнуть.'
                              ' Сейчас подберу что-нибудь'
                              ' подходящее.')
        activity = 'chill'


@bot.message_handler(content_types=['text'])  # Ловец апдейтов (новые сообщения или редактирование)
@bot.edited_message_handler(content_types=['text'])
def text_handler(message: Message):
    if 'выбрать город' in message.text.lower():
        city_ask(message)
    elif 'погода' in message.text.lower():
        if city == 'swamp':
            bot.send_message(message.chat.id,
                             f'Сегодня {forecasts_swamp[0].text},'
                             ' ожидается темпаратура'
                             f' от {forecasts_swamp[0].low}'
                             f' до {forecasts_swamp[0].high}'
                             ' по Цельсию.')
        elif city == 'moscow':
            bot.send_message(message.chat.id,
                             f'Сегодня {forecasts_moscow[0].text},'
                             ' ожидается темпаратура'
                             f' от {forecasts_moscow[0].low}'
                             f' до {forecasts_moscow[0].high}'
                             ' по Цельсию.')
    elif 'дайджест' in message.text.lower():
        digest(message)
    elif 'привет' in message.text.lower():
        bot.send_message(message.chat.id, 'Тебе тоже привет!')
    else:
        bot.send_message(message.chat.id, 'Прости, я тебя не понимаю')


print('Ну че, погнали?')
bot.polling(timeout=60)  # Ожидаем респонса
