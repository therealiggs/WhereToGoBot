import telebot
from telebot.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
# import os
import time
from weather import Weather, Unit


weather = Weather(unit=Unit.CELSIUS)
forecasts_moscow = weather.lookup_by_location('moscow').forecast
forecasts_swamp = weather.lookup_by_location('petersburg').forecast
# Здесь с помощью weather-api предзагружаем прогноз погоды,
# т.к. библиотека не работает через прокси
'''
os.startfile(os.path.dirname(__file__) + "/Ultrasurf.exe")
# После чего запускаем прокси. fck da Роскомнадзор
time.sleep(15)  # Время, чтобы соединение стабилизировалось.
#  За 10 секунд оно не всегда успевает
'''
city = activity = None
token = '776536658:AAHuHAi28nhFCKyGgASAHWd-063hyItVEmQ'
bot = telebot.TeleBot(token)


def activity_ask(message: Message):  # Выбор типа активности, флекс или же чилл
    keyboard = InlineKeyboardMarkup()
    button_flex = InlineKeyboardButton(text='🤩',
                                       callback_data='set_activity_flex')
    button_chill = InlineKeyboardButton(text='🤤',
                                        callback_data='set_activity_chill')
    keyboard.add(button_flex, button_chill)
    bot.send_message(message.chat.id, text='Флексить или чиллить?'
                                           ' Пора определиться!',
                     reply_markup=keyboard)


def city_ask(message: Message):  # Выбор города
    keyboard = InlineKeyboardMarkup()
    button_moscow = InlineKeyboardButton(text='Москва',
                                         callback_data="set_city_moscow")
    button_swamp = InlineKeyboardButton(text='Боло.. Ой, СПб',
                                        callback_data="set_city_swamp")
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


def act_list(message: Message):
    global city, activity
    date = time.ctime(time.time())
    day = date[:3]
    month = date[4:7]
    hour = date[11:13]
    weekend = ['Sat', 'Sun']

    if city == 'moscow':
        bot.send_message(chat_id=message.chat.id,
                         text='Контент для вашего города'
                              ' находится на стадии разработки.')
    else:
        if '18' > hour > '08':
            if activity == 'flex':
                if day in weekend:
                    bot.send_message(chat_id=message.chat.id,
                                     text='Лучший флекс в выходные? '
                                          'WRAVE, естественно.'
                                          'Сумасшедшие тусовки '
                                          'от профессионалов в '
                                          'популярных клубах с '
                                          'приглашёнными диджеями '
                                          'не оставят вам шанса заскучать. '
                                          'Следите за событиями '
                                          'в оффициальном инстаграмме: '
                                          'https://www.instagram.com/_wrave_/'
                                          ' (На правах рекламы.)')
                else:
                    bot.send_message(chat_id=message.chat.id,
                                     text='Флексить в такое время '
                                          'особо негде...'
                                          'Может, пока почиллим? '
                                          'А там гляди откроются '
                                          'какие-нибудь бары... '
                                          '/activity_set')
            elif activity == 'chill':
                if month in ['Jan', 'Feb', 'Dec']:  # Зимние спокойные
                    #  развлечения
                    bot.send_message(chat_id=message.chat.id,
                                     text='Традиционное зимнее '
                                          'развлечение в Петербурге -'
                                          ' конечно же Шуваловка! '
                                          'Погрузитесь в аутентичную'
                                          ' атмосферу древнерусской '
                                          'Масленицы: пройдитесь по'
                                          ' ярморочным лавочкам '
                                          'испытайте удачу в конкурсах '
                                          'или попробуйте себя в кузнечном'
                                          ' деле! Также в наличии склоны'
                                          ' для санок, ватрушек и всего,'
                                          ' чего вам вздумается. '
                                          'http://www.shuvalovka.ru/')

                    bot.send_message(chat_id=message.chat.id,
                                     text='Если лень ехать в Шуваловку, '
                                          'всегда можно насладиться'
                                          ' великолепием зимнего леса прямо'
                                          ' посреди спального района,'
                                          ' ведь по размерам Сосновка'
                                          ' - скорее лес, чем обычный'
                                          ' парк. Зимой здесь особенно'
                                          ' красиво,но не забывайте'
                                          ' одеться потеплее! '
                                          'bit.ly/Sosnovka')

                    bot.send_message(chat_id=message.chat.id,
                                     text='Как бы холодно не было на улице,'
                                          'всегда можно сходить в кино.'
                                          'Смотрите новинки в кинотеатрах'
                                          ' Петербурга: '
                                          'https://kinoteatr.ru/')

                else:
                    bot.send_message(chat_id=message.chat.id,
                                     text='Хоть лично я и предпочитаю'
                                          ' гулять в Сосновке зимой,'
                                          'там красиво круглый год.'
                                          ' Снегопады сменяются весенними '
                                          'первоцветами или листопадами,'
                                          ' а летом даже можно купаться в '
                                          'местном пруду. Насладиться'
                                          ' природой здесь можно всегда: '
                                          'bit.ly/Sosnovka')

                    bot.send_message(chat_id=message.chat.id,
                                     text='Если погода сносная, можно'
                                          ' посетить Диво-Остров - '
                                          'отличный парк атракционов'
                                          ' где и дети и взрослые найдут '
                                          'себе что-нибудь по вкусу.'
                                          ' Для адреналиновых наркоманов'
                                          ' от автора'
                                          'лично рекомендуется атракцион'
                                          ' Великолукского Мясокомбината - '
                                          'с покерфейсом оттуда'
                                          ' вы уж точно не выйдете. '
                                          'https://www.divo-ostrov.ru/')
            else:
                bot.send_message(chat_id=message.chat.id,
                                 text='Пожалуйста, выберите '
                                      'тип активности: /activity_set')

        else:
            if activity == 'flex':
                bot.send_message(chat_id=message.chat.id,
                                 text='Не знаешь где пофлексить'
                                      ' - иди в Молодость и зови всех '
                                      'друзей. Одни из лучших,'
                                      ' если не лучшие, кальяны в городе и '
                                      'распологающая атмосфера'
                                      ' не дадут заскучать. '
                                      'https://vk.com/spbmolodost')
                bot.send_message(chat_id=message.chat.id,
                                 text='Бар - это всегда хорошо, а'
                                      ' если бар - это Буковски, то хорошо '
                                      'вдвойне. Крафтовый стаут здесь'
                                      ' течёт по усам только так.'
                                      ' Огромный лайк '
                                      'лично от автора. http://russiancraf'
                                      'tbeer.ru/place/bukowski-bar')

            elif activity == 'chill':
                bot.send_message(chat_id=message.chat.id,
                                 text='Ночной Питер - что может быть'
                                      ' романтичнее? Отправляйтесь в центр'
                                      'и прогуляйтесь по набережным, ну'
                                      ' или просто пройдите по Невскому: '
                                      'одни только уличные музыканты чего'
                                      ' стоят... Личный респект группе'
                                      ' Штрудель от автора, ищите их на'
                                      ' углу Думской и Невского в долгие'
                                      ' питерские вечера. Группа Штрудель:'
                                      ' https://vk.com/shtruedel')

            else:
                bot.send_message(chat_id=message.chat.id,
                                 text='Пожалуйста, выберите тип'
                                      ' активности: /activity_set')


@bot.message_handler(commands=['help'])  # Ловец команлы help
def command_handler(message: Message):
    bot.send_message(message.chat.id, 'Поддерживаются команды: /help /start '
                                      'Поддерживаются ключевые слова: '
                                      'выбрать город, дайджест, погода, '
                                      'куда сходить')


@bot.message_handler(commands=['start'])  # Ловец команды start
def command_handler(message: Message):
    city_ask(message)


@bot.message_handler(commands=['activity_set'])  # Ловец команды start
def command_handler(message: Message):
    activity_ask(message)


@bot.callback_query_handler(func=lambda call: True)  # Ловец кнопок
def callback_inline(call):
    if call.data.startswith('set_city_'):
        global city, activity
        if call.data == 'set_city_moscow':
            city = 'moscow'
            bot.send_message(chat_id=call.message.chat.id,
                             text='Контент для вашего города'
                                  ' находится на стадии разработки.')
        else:
            bot.send_message(chat_id=call.message.chat.id,
                             text='Город успешно выбран!')
            city = 'swamp'
            activity_ask(call.message)

    elif call.data == 'set_activity_flex':
        bot.send_message(chat_id=call.message.chat.id,
                         text='Значит, сегодня зажигаем!'
                              ' Сейчас подберу что-нибудь'
                              ' подходящее.')
        activity = 'flex'
        act_list(call.message)

    elif call.data == 'set_activity_chill':
        bot.send_message(chat_id=call.message.chat.id,
                         text='Время как следует отдохнуть.'
                              ' Сейчас подберу что-нибудь'
                              ' подходящее.')
        activity = 'chill'
        act_list(call.message)


@bot.message_handler(content_types=['text'])  # Ловец апдейтов (новые
#  сообщения  или редактирование)
@bot.edited_message_handler(content_types=['text'])
def text_handler(message: Message):
    if 'выбрать город' in message.text.lower():
        city_ask(message)
    elif 'куда пойти' in message.text.lower():
        act_list(message)
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
        else:
            bot.send_message(message.chat.id, 'Похоже, вы еще'
                                              ' не выбрали город.'
                                              ' Начнём прямо сейчас?'
                                              ' /start')
    elif 'дайджест' in message.text.lower():
        digest(message)
    elif 'привет' in message.text.lower():
        bot.send_message(message.chat.id, 'Тебе тоже привет!')
    else:
        bot.send_message(message.chat.id, 'Прости, я тебя не понимаю')


print('Ну че, погнали?')
bot.polling(timeout=60)  # Ожидаем респонса
