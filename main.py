import telebot
from telebot import types
import psycopg2
from searchweek import week

token = "2101563392:AAEdccoATp-o1_rqcgG4N1dyrD8nDn1qXCg"
bot = telebot.TeleBot(token)

conn = psycopg2.connect(database="LessonRaspis",
                        user="postgres",
                        password="426572",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()
today = int(week())


@bot.message_handler(commands=['start'])
def start_message(message):
   if today == 0:
       bot.send_message(message.chat.id, 'Добрый день, на какую день вы хотите узнать расписание пар ?'
                                         '\n\nСейчас четная (нижняя) неделя',reply_markup=keyboardodd())
   elif today == 1:
       bot.send_message(message.chat.id, 'Добрый день, на какую день вы хотите узнать расписание пар ?'
                                         '\n\nСейчас нечетная (верхняя) неделя',reply_markup=keyboardeven())
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Это бот, созданный для определения расписания у группы БИН2008'
                                      '\n\nЧтобы узнать расписание на день, достаточно написать /start, либо нажать на одноименную кнопку и правильно нажимать на следующие кнопки'
                                      '\nКоманды:'
                                      '\n/week - узнать текущую неделю'
                                      '\n/mtuci - вывести ссылку на официальный сайт МТУСИ')

@bot.message_handler(commands=['mtuci'])
def mtuci_message(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru/')

@bot.message_handler(commands=['week'])
def week_message(message):
    if today == 0:
        bot.send_message(message.chat.id, 'Текущая неделя - четная')
    elif today == 1:
        bot.send_message(message.chat.id, 'Текущая неделя - нечетная')

@bot.message_handler(commands=['button'])
async def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("button")
    markup.add(item1)
    await message.answer("Выберите действие", reply_markup=markup)

def keyboardeven():
    buttn1 = types.KeyboardButton('Понедельник 📖')
    buttn2 = types.KeyboardButton('Вторник 📖')
    buttn3 = types.KeyboardButton('Среда 📖')
    buttn4 = types.KeyboardButton('Четверг 📖')
    buttn5 = types.KeyboardButton('Пятница 📖')
    butnn1 = types.KeyboardButton('📖Расписание на текущую неделю📖')
    butnn2 = types.KeyboardButton('📖Расписание на следующую неделю📖')
    button5 = types.KeyboardButton('🔁 Вернуться к неделям 🔁')
    markup2 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(buttn1).add(buttn2).add(buttn3).add(buttn4).add(buttn5).add(button5).add(butnn1).add(butnn2)
    return(markup2)

def keyboardodd():
    butn1 = types.KeyboardButton('📖 Понедельник')
    butn2 = types.KeyboardButton('📖 Вторник')
    butn3 = types.KeyboardButton('📖 Среда')
    butn4 = types.KeyboardButton('📖 Четверг')
    butn5 = types.KeyboardButton('📖 Пятница')
    butnn1 = types.KeyboardButton('📖Расписание на текущую неделю📖')
    butnn2 = types.KeyboardButton('📖Расписание на следующую неделю📖')
    button5 = types.KeyboardButton('🔁 Вернуться к неделям 🔁')
    markup3 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(butn1).add(butn2).add(
        butn3).add(butn4).add(butn5).add(button5).add(butnn1).add(butnn2)
    return markup3

def returner():
    rtrn = types.KeyboardButton('🔁 Вернуться к выбору недели 🔁')
    markup6 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(rtrn)
    return markup6

@bot.message_handler(content_types=['text'])
def manipulator(message):
    if message.text == 'Четная':
        bot.send_message(message.chat.id, 'Выбери день недели', reply_markup=keyboardodd())
    elif message.text == 'Нечетная':
        bot.send_message(message.chat.id, 'Выбери день недели', reply_markup=keyboardeven())
    elif message.text == '🔁 Вернуться к неделям 🔁':
        if today == 0:
            bot.send_message(message.chat.id, 'Добрый день, на какую день вы хотите узнать расписание пар ?'
                                              '\n\nСейчас четная (нижняя) неделя', reply_markup=keyboardodd())
        elif today == 1:
            bot.send_message(message.chat.id, 'Добрый день, на какую день вы хотите узнать расписание пар ?'
                                              '\n\nСейчас нечетная (верхняя) неделя', reply_markup=keyboardeven())
    elif message.text == '🔁 Вернуться к выбору недели 🔁':
        if today == 0:
            bot.send_message(message.chat.id, 'Добрый день, на какую день вы хотите узнать расписание пар ?'
                                              '\n\nСейчас четная (нижняя) неделя', reply_markup=keyboardodd())
        elif today == 1:
            bot.send_message(message.chat.id, 'Добрый день, на какую день вы хотите узнать расписание пар ?'
                                              '\n\nСейчас нечетная (верхняя) неделя', reply_markup=keyboardeven())
    elif message.text == '📖 Понедельник':
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='Понедельник'")
        x = cursor.fetchall()
        x1 = str('Понедельник, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=returner())
    elif message.text == '📖 Вторник':
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ВторникНЧ'")
        x = cursor.fetchall()
        x1 = str('Вторник, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=returner())
    elif message.text == '📖 Среда':
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='СредаНЧ'")
        x = cursor.fetchall()
        x1 = str('Среда, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=returner())
    elif message.text == '📖 Четверг':
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ЧетвергНЧ'")
        x = cursor.fetchall()
        x1 = str('Четверг, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=returner())
    elif message.text == '📖 Пятница':
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ПятницаНЧ'")
        x = cursor.fetchall()
        x1 = str('Пятница, верхняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=returner())
    elif message.text == 'Понедельник 📖':
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='Понедельник'")
        x = cursor.fetchall()
        x1 = str('Понедельник, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=returner())
    elif message.text == 'Вторник 📖':
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ВторникЧ'")
        x = cursor.fetchall()
        x1 = str('Вторник, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=returner())
    elif message.text == 'Среда 📖':
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='СредаЧ'")
        x = cursor.fetchall()
        x1 = str('Среда, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=returner())
    elif message.text == 'Четверг 📖':
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ЧетвергЧ'")
        x = cursor.fetchall()
        x1 = str('Четверг, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=returner())
    elif message.text == 'Пятница 📖':
        cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ПятницаЧ'")
        x = cursor.fetchall()
        x1 = str('Пятница, нижняя неделя\n\n\n')
        for row in x:
            for i in range(4):
                x1 += str(row[i]) + '    '
            x1 += '\n\n'
        bot.send_message(message.chat.id, x1, reply_markup=returner())
    elif message.text == '📖Расписание на текущую неделю📖':
        if today == 1:
            cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='Понедельник'")
            x = cursor.fetchall()
            x1 = str('Понедельник, верхняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ВторникЧ'")
            x = cursor.fetchall()
            x1 = str('Вторник, верхняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='СредаЧ'")
            x = cursor.fetchall()
            x1 = str('Среда, верхняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ЧетвергЧ'")
            x = cursor.fetchall()
            x1 = str('Четверг, верхняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ПятницаЧ'")
            x = cursor.fetchall()
            x1 = str('Пятница, верхняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1, reply_markup=returner())
        elif today == 0:
            cursor.execute(
                "SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='Понедельник'")
            x = cursor.fetchall()
            x1 = str('Понедельник, нижняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute(
                "SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ВторникНЧ'")
            x = cursor.fetchall()
            x1 = str('Вторник, нижняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute(
                "SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='СредаНЧ'")
            x = cursor.fetchall()
            x1 = str('Среда, нижняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute(
                "SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ЧетвергНЧ'")
            x = cursor.fetchall()
            x1 = str('Четверг, нижняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute(
                "SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ПятницаНЧ'")
            x = cursor.fetchall()
            x1 = str('Пятница, нижняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1, reply_markup=returner())
    elif message.text == '📖Расписание на следующую неделю📖':
        if today == 0:
            cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='Понедельник'")
            x = cursor.fetchall()
            x1 = str('Понедельник, верхняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ВторникЧ'")
            x = cursor.fetchall()
            x1 = str('Вторник, верхняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='СредаЧ'")
            x = cursor.fetchall()
            x1 = str('Среда, верхняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ЧетвергЧ'")
            x = cursor.fetchall()
            x1 = str('Четверг, верхняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute("SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ПятницаЧ'")
            x = cursor.fetchall()
            x1 = str('Пятница, верхняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1, reply_markup=returner())
        elif today == 1:
            cursor.execute(
                "SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='Понедельник'")
            x = cursor.fetchall()
            x1 = str('Понедельник, нижняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute(
                "SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ВторникНЧ'")
            x = cursor.fetchall()
            x1 = str('Вторник, нижняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute(
                "SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='СредаНЧ'")
            x = cursor.fetchall()
            x1 = str('Среда, нижняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute(
                "SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ЧетвергНЧ'")
            x = cursor.fetchall()
            x1 = str('Четверг, нижняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1)
            cursor.execute(
                "SELECT timetable.start, timetable.subject, timetable.room, teacher.full_name FROM public.timetable JOIN public.teacher ON timetable.teacher = teacher.id WHERE day ='ПятницаНЧ'")
            x = cursor.fetchall()
            x1 = str('Пятница, нижняя неделя\n\n\n')
            for row in x:
                for i in range(4):
                    x1 += str(row[i]) + '    '
                x1 += '\n\n'
            bot.send_message(message.chat.id, x1, reply_markup=returner())
    else:
        bot.send_message(message.chat.id, 'Прости, но я создан для выдачи расписания, а не общения. Да, мир бывает жесток... Лучше спроси у меня расписание')
        bot.send_message(message.chat.id, 'На какую неделю ты хочешь узнать расписание пар ?',reply_markup=keyboard())

bot.infinity_polling()
