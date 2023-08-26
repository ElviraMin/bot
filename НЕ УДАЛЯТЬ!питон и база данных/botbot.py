import psycopg2
import telebot
from telebot import types
bot = telebot.TeleBot('6561176643:AAH3fXP9bTjBF_AZfGbDJgaIZceeXE0qRZI')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    try:
        connection = psycopg2.connect(host = 'localhost',dbname = "itrun",user = "postgres",password = "0770757702" )
        cursor = connection.cursor()
        query = f"INSERT INTO messages(message, user_telegram_id) values('{message.text}', '{message.from_user.id}');"
        cursor.execute(query)
        connection.commit()

        query = f"SELECT * FROM courses;"
        cursor.execute(query)
        connection.commit()
        rows = cursor.fetchall()

        кнопки = types.InlineKeyboardMarkup()
        for row in rows:
            кнопка = types.InlineKeyboardButton(f"{row[1]}", callback_data=f'{row[0]}')
            кнопки.add(кнопка)
        bot.send_message(message.from_user.id, f"Здравствуйте, выберите действие", reply_markup=кнопки)

    except Exception as e:
        print("Возникла ошибка")
        print(e)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            connection = psycopg2.connect(host = 'localhost',dbname = "itrun",user = "postgres",password = "0770757702" )
            cursor = connection.cursor()
            query = f"SELECT * FROM courses WHERE id = {call.data} LIMIT 1;"
            cursor.execute(query)
            rows = cursor.fetchall()

            bot.send_message(call.message.chat.id, f'{rows[0][2]}')

            query = f"SELECT * FROM lessons WHERE course_id = {call.data} AND date>NOW() LIMIT 5;"
            cursor.execute(query)
            lessons = cursor.fetchall()

            for row in lessons:
                bot.send_message(call.message.chat.id, f'Урок на тему: {row[1]}, начало в {row[2]}')

    except:
        print('Ошибка')


bot.polling(none_stop=True, interval=0)