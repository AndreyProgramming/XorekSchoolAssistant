#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import time
import sqlite3
from telebot import types
 
bot = telebot.TeleBot('YOUR_TOKEN')     

@bot.message_handler(commands=['start'])
def welcome(message):
	db = sqlite3.connect('ids.db')
	sql = db.cursor()
	sql.execute("""CREATE TABLE IF NOT EXISTS users (
		id TEXT
	)""")
	db.commit()

	sql.execute("SELECT id FROM users")
	res = sql.fetchall()
	for i in res:
		if list(i[0].split(" "))[0] == str(message.from_user.id):
			alrdexist = True
			break
		else:
			alrdexist = False
	if res == []:
		alrdexist = False

	sql.execute("SELECT DISTINCT id FROM users WHERE id = '{users_id}'")
	if sql.fetchone() is None:
		if alrdexist == False:
			sql.execute("INSERT INTO users VALUES (?)", (message.from_user.id,))
			db.commit()
		else:
			pass
	else:
		print('Already exist')
	db.commit()



	db = sqlite3.connect('ids.db')
	sql = db.cursor()
	sql.execute("""CREATE TABLE IF NOT EXISTS users_nicks (
		nick TEXT
	)""")
	db.commit()

	sql.execute("SELECT DISTINCT nick FROM users_nicks WHERE nick = '{users_nicks_nick}'")
	if sql.fetchone() is None:
		if alrdexist == False:
			sql.execute("INSERT INTO users_nicks VALUES (?)", (message.from_user.username,))
			db.commit()
		else:
			pass
	else:
		print('Already exist')
	db.commit()



	db = sqlite3.connect('ids.db')
	sql = db.cursor()
	sql.execute("""CREATE TABLE IF NOT EXISTS first_names (
		f_name TEXT
	)""")
	db.commit()

	sql.execute("SELECT DISTINCT f_name FROM first_names WHERE f_name = '{f_names}'")
	if sql.fetchone() is None:
		if alrdexist == False:
			sql.execute("INSERT INTO first_names VALUES (?)", (message.from_user.first_name,))
			db.commit()
		else:
			pass
	else:
		print('Already exist')
	db.commit()



	db = sqlite3.connect('ids.db')
	sql = db.cursor()
	sql.execute("""CREATE TABLE IF NOT EXISTS l_names (
		l_name TEXT
	)""")
	db.commit()

	sql.execute("SELECT DISTINCT l_name FROM l_names WHERE l_name = '{l_names}'")
	if sql.fetchone() is None:
		if alrdexist == False:
			sql.execute("INSERT INTO l_names VALUES (?)", (message.from_user.last_name,))
			db.commit()
		else:
			pass
	else:
		print('Already exist')
	db.commit()



	#Создание клавиатуры для выбора функций
	markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
	#item1 = types.KeyboardButton("Переводчик (В РАЗРАБОТКЕ)")
	item2 = types.KeyboardButton("Расписание")
	item3 = types.KeyboardButton("Расписание звонков")
	item4 = types.KeyboardButton("О разработчиках")

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот чтобы помогать во время учебы.".format(message.from_user, bot.get_me()), parse_mode='html')
	time.sleep(1)

	#Подключение клавиатуры 
	markup_start.add(item2, item3)
	#markup_start.row(item1)
	markup_start.row(item4)

	bot.send_message(message.chat.id, "Выберите нужную функцию: ", reply_markup = markup_start)


#@bot.message_handler(func=lambda m: m.text=='На англиский', content_types=['text'])
#def langeng(message):
	#msg_two = bot.send_message(message.chat.id, "Введите текст который нужно перевести: ")
	#bot.register_next_step_handler(msg_two, func_two)

#def func_two(message):
	#translator = Translator()
	#result = translator.translate(message.text, src='ru', dest='en')
	#msg_two = bot.send_message(message.chat.id, result.text)


@bot.message_handler(func=lambda m: m.text=='О разработчиках', content_types=['text'])
def about(message):
	bot.send_message(message.chat.id, "Здравствуй!!\nМы не большая, но команда разработчиков Xorek Developer.\n\nОсновная часть кода:\nБурдин Андрей;\n\nРевью кода и поддержка в функционале:\nАманжолов Рустам;\n\nНа разработку бота ушло 4 полных дня, не учитывая сон и тд.\n\nПри возможных ошибках багов и тд. просьба писать сюда: @programmingda\n\nДля поддержки и донатов:\n5375 4188 0447 7321")




@bot.message_handler(func=lambda m: m.text=='Расписание звонков', content_types=['text'])
def timetable_ofbell(message):
	markup_smens = types.ReplyKeyboardMarkup(resize_keyboard=True)
	smen1 = types.KeyboardButton("| смена")
	smen2 = types.KeyboardButton("|| смена")
	smen_fuction = types.KeyboardButton("Назад к функциям")

	markup_smens.add(smen1, smen2)
	markup_smens.row(smen_fuction)

	bot.send_message(message.chat.id, "Выберите свою смену: ", reply_markup = markup_smens)

@bot.message_handler(func=lambda m: m.text=='| смена', content_types=['text'])
def timetable_ofbell_one(message):
	bot.send_message(message.chat.id, "1 урок: 8:00 - 8:35\n\n2 урок: 8:45 - 9:20\n\n3 урок: 9:35 - 10:10\n\n4 урок: 10:25 - 11:00\n\n5 урок: 11:10 - 11:45\n\n6 урок: 12:00 - 12:35\n\n7 урок: 12:45 - 13:20\n")


@bot.message_handler(func=lambda m: m.text=='|| смена', content_types=['text'])
def timetable_ofbell_two(message):
	bot.send_message(message.chat.id, "1 урок: 12:00 - 12:35\n\n2 урок: 12:45 - 13:20\n\n3 урок: 13:30 - 14:05\n\n4 урок: 14:15 - 14:50\n\n5 урок: 15:00 - 15:35\n\n6 урок: 15:45 - 16:20\n\n7 урок: 16:30 - 17:05\n")




@bot.message_handler(func=lambda m: m.text=='Расписание', content_types=['text'])
def timetable(message):
	bot.send_message(message.chat.id, "Открываем классы...")
	time.sleep(1)

	#Создание клавиатуры для выбора функций
	markup_classes = types.ReplyKeyboardMarkup(resize_keyboard=True)
	classs8a = types.KeyboardButton("8 A класс")
	classs8b = types.KeyboardButton("8 Б класс")
	classs9 = types.KeyboardButton("9 A класс")
	classs10 = types.KeyboardButton("9 Б класс")
	classs11 = types.KeyboardButton("10 класс")
	classsinfuction = types.KeyboardButton("Назад к функциям")

	#Подключение клавиатуры
	markup_classes.row(classs8a, classs8b) 
	markup_classes.row(classs9, classs10, classs11)
	markup_classes.row(classsinfuction)
	bot.send_message(message.chat.id, "Выберите свой класс: ", reply_markup = markup_classes)




@bot.message_handler(func=lambda m: m.text=='8 A класс', content_types=['text'])
def eightA_class(message):
	#Создание клавиатуры для выбора функций
	markup_days_for_eightA = types.ReplyKeyboardMarkup(resize_keyboard=True)
	first_day_eightA = types.KeyboardButton("Понедельник - (8А)")
	secound_day_eightA = types.KeyboardButton("Вторник - (8А)")
	third_day_eightA = types.KeyboardButton("Среда - (8А)")
	fourth_day_eightA = types.KeyboardButton("Четверг - (8А)")
	fifth_day_eightA = types.KeyboardButton("Пятница - (8А)")
	returning_eightA = types.KeyboardButton("Назад к классам")

	#Подключение клавиатуры
	markup_days_for_eightA.row(first_day_eightA)
	markup_days_for_eightA.add(secound_day_eightA, third_day_eightA, fourth_day_eightA, fifth_day_eightA)
	markup_days_for_eightA.row(returning_eightA)

	bot.send_message(message.chat.id, "Выберите день недели: ", reply_markup = markup_days_for_eightA)

@bot.message_handler(func=lambda m: m.text=='Понедельник - (8А)', content_types=['text'])
def ponedelnik(message):
	bot.send_message(message.chat.id, "1) Англійська мова\n2) Зарубіжна література\n3) Українська мова\n4) Фізкультура\n5) Історія\n6) Українська література\n7) Історія\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Вторник - (8А)', content_types=['text'])
def vtornik(message):
	bot.send_message(message.chat.id, "1) Алгебра\n2) Геометрія\n3) Мистецтво\n4) Інформатика\n5) Англійська мова\n6) Географія\n7) Трудове навчання\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Среда - (8А)', content_types=['text'])
def sreda(message):
	bot.send_message(message.chat.id, "1) Хімія\n2) Біологія\n3) Основи здоров'я\n4) Фізика\n5) Фізкультура\n6) Географія\n\n6 уроків")


@bot.message_handler(func=lambda m: m.text=='Четверг - (8А)', content_types=['text'])
def chetverg(message):
	bot.send_message(message.chat.id, "1) Алгебра\n2) Геометрія\n3) Українська мова\n4) Українська література\n5) Фізкультура\n6) Інформатика\n\n6 уроків")


@bot.message_handler(func=lambda m: m.text=='Пятница - (8А)', content_types=['text'])
def pyatnica(message):
	bot.send_message(message.chat.id, "1) Фізика\n2) Хімія\n3) Історія\n4) Зарубіжна література\n5) Біологія\n6) Англійська мова\n\n6 уроків")


@bot.message_handler(func=lambda m: m.text=='Назад к классам', content_types=['text'])
def pyatnica(message):
	bot.send_message(message.chat.id, "Возвращаемся...")
	timetable(message)




@bot.message_handler(func=lambda m: m.text=='8 Б класс', content_types=['text'])
def eightB_class(message):
	#Создание клавиатуры для выбора функций
	markup_days_for_eight_B = types.ReplyKeyboardMarkup(resize_keyboard=True)
	first_day_eightB = types.KeyboardButton("Понедельник - (8Б)")
	secound_day_eightB = types.KeyboardButton("Вторник - (8Б)")
	third_day_eightB = types.KeyboardButton("Среда - (8Б)")
	fourth_day_eightB = types.KeyboardButton("Четверг - (8Б)")
	fifth_day_eightB = types.KeyboardButton("Пятница - (8Б)")
	returning_eightB = types.KeyboardButton("Назад к классам")

	#Подключение клавиатуры
	markup_days_for_eight_B.row(first_day_eightB)
	markup_days_for_eight_B.add(secound_day_eightB, third_day_eightB, fourth_day_eightB, fifth_day_eightB)
	markup_days_for_eight_B.row(returning_eightB)

	bot.send_message(message.chat.id, "Выберите день недели: ", reply_markup = markup_days_for_eight_B)

@bot.message_handler(func=lambda m: m.text=='Понедельник - (8Б)', content_types=['text'])
def ponedelnik(message):
	bot.send_message(message.chat.id, "1) Зарубіжна література\n2) Фізкультура\n3) Хімія\n4) Українська мова\n5) Українська література\n6) Історія\n7) Історія\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Вторник - (8Б)', content_types=['text'])
def vtornik(message):
	bot.send_message(message.chat.id, "1) Англійська мова\n2) Інформатика\n3) Трудове навчання\n4) Алгебра\n5) Геометрія\n6) Основи здоров'я\n\n6 уроків")


@bot.message_handler(func=lambda m: m.text=='Среда - (8Б)', content_types=['text'])
def sreda(message):
	bot.send_message(message.chat.id, "1) Фізика\n2) Фізкультура\n3) Англійська мова\n4) Географія\n5) Хімія\n6) Біологія\n\n6 уроків")


@bot.message_handler(func=lambda m: m.text=='Четверг - (8Б)', content_types=['text'])
def chetverg(message):
	bot.send_message(message.chat.id, "1) Українська мова\n2) Українська література\n3) Інформатика\n4) Алгебра\n5) Геометрія\n6) Біологія\n7) Фізкультура\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Пятница - (8Б)', content_types=['text'])
def pyatnica(message):
	bot.send_message(message.chat.id, "1) Зарубіжна література\n2) Мистецтво\n3) Англійська мова\n4) Історія\n5) Фізика\n6) Географія\n\n6 уроків")


@bot.message_handler(func=lambda m: m.text=='Назад к классам', content_types=['text'])
def pyatnica(message):
	bot.send_message(message.chat.id, "Возвращаемся...")
	timetable(message)




@bot.message_handler(func=lambda m: m.text=='9 A класс', content_types=['text'])
def nineA_class(message):
	#Создание клавиатуры для выбора функций
	markup_days_for_nine_A = types.ReplyKeyboardMarkup(resize_keyboard=True)
	first_day_A = types.KeyboardButton("Понедельник - (9А)")
	secound_day_A = types.KeyboardButton("Вторник - (9А)")
	third_day_A = types.KeyboardButton("Среда - (9А)")
	fourth_day_A = types.KeyboardButton("Четверг - (9А)")
	fifth_day_A = types.KeyboardButton("Пятница - (9А)")
	returning_A = types.KeyboardButton("Назад к классам")

	#Подключение клавиатуры
	markup_days_for_nine_A.row(first_day_A)
	markup_days_for_nine_A.add(secound_day_A, third_day_A, fourth_day_A, fifth_day_A)
	markup_days_for_nine_A.row(returning_A)

	bot.send_message(message.chat.id, "Выберите день недели: ", reply_markup = markup_days_for_nine_A)

@bot.message_handler(func=lambda m: m.text=='Понедельник - (9А)', content_types=['text'])
def ponedelnik(message):
	bot.send_message(message.chat.id, "1) Біологія\n2) Хімія\n3) Англійська Мова\n4) Фізика\n5) Українська мова\n6) Українська література\n7) Українська література\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Вторник - (9А)', content_types=['text'])
def vtornik(message):
	bot.send_message(message.chat.id, "1) Інформатика\n2) Фізкультура\n3) Основи здоров'я\n4) Трудове навчання\n5) Алгебра\n6) Геометрія\n7) Мистецтво\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Среда - (9А)', content_types=['text'])
def sreda(message):
	bot.send_message(message.chat.id, "1) Фізика\n2) Хімія\n3) Біологія\n4) Англійська мова\n5) Зарубіжна література\n6) Історія\n7) Фізкультура\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Четверг - (9А)', content_types=['text'])
def chetverg(message):
	bot.send_message(message.chat.id, "1) Українська мова\n2) Українська мова\n3) Українська література\n4) Правознавство\n5) Алгебра\n6) Геометрія\n7) Інформатика\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Пятница - (9А)', content_types=['text'])
def pyatnica(message):
	bot.send_message(message.chat.id, "1) Англійська мова\n2) Історія\n3) Географія\n4) Фізика\n5) Фізкультура\n6) Зарубіжна література\n7) Географія/Історія\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Назад к классам', content_types=['text'])
def pyatnica(message):
	bot.send_message(message.chat.id, "Возвращаемся...")
	timetable(message)




@bot.message_handler(func=lambda m: m.text=='9 Б класс', content_types=['text'])
def nineB_class(message):
	#Создание клавиатуры для выбора функций
	markup_days_for_nine_B = types.ReplyKeyboardMarkup(resize_keyboard=True)
	first_day_B = types.KeyboardButton("Понедельник - (9Б)")
	secound_day_B = types.KeyboardButton("Вторник - (9Б)")
	third_day_B = types.KeyboardButton("Среда - (9Б)")
	fourth_day_B = types.KeyboardButton("Четверг - (9Б)")
	fifth_day_B = types.KeyboardButton("Пятница - (9Б)")
	returning_B = types.KeyboardButton("Назад к классам")

	#Подключение клавиатуры
	markup_days_for_nine_B.row(first_day_B)
	markup_days_for_nine_B.add(secound_day_B, third_day_B, fourth_day_B, fifth_day_B)
	markup_days_for_nine_B.row(returning_B)

	bot.send_message(message.chat.id, "Выберите день недели: ", reply_markup = markup_days_for_nine_B)

@bot.message_handler(func=lambda m: m.text=='Понедельник - (9Б)', content_types=['text'])
def ponedelnik(message):
	bot.send_message(message.chat.id, "1) Фізкультура\n2) Англійська мова\n3) Українська мова\n4) Українська література\n5) Фізика\n6) Хімія\n7) Біологія\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Вторник - (9Б)', content_types=['text'])
def vtornik(message):
	bot.send_message(message.chat.id, "1) Історія\n2) Основи здоров'я\n3) Алгебра\n4) Геометрія\n5) Трудове навчання\n6) Географія\n7) Географія\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Среда - (9Б)', content_types=['text'])
def sreda(message):
	bot.send_message(message.chat.id, "1) Англійська мова\n2) Зарубіжна література\n3) Фізика\n4) Інформатика\n5) Хімія\n6) Біологія\n\n6 уроків")


@bot.message_handler(func=lambda m: m.text=='Четверг - (9Б)', content_types=['text'])
def chetverg(message):
	bot.send_message(message.chat.id, "1) Фізкультура\n2) Алгебра\n3) Геометрія\n4) Українська мова\n5) Українська література\n6) Інформатика\n7) Правознавство\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Пятница - (9Б)', content_types=['text'])
def pyatnica(message):
	bot.send_message(message.chat.id, "1) Фізкультура\n2) Англійська мова\n3) Фізика\n4) Зарубіжна література\n5) Мистецтво\n6) Історія\n7) Історія\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Назад к классам', content_types=['text'])
def pyatnica(message):
	bot.send_message(message.chat.id, "Возвращаемся...")
	timetable(message)




@bot.message_handler(func=lambda m: m.text=='10 класс', content_types=['text'])
def nineB_class(message):
	#Создание клавиатуры для выбора функций
	markup_days_for_ten = types.ReplyKeyboardMarkup(resize_keyboard=True)
	first_day_ten = types.KeyboardButton("Понедельник - (10)")
	secound_day_ten = types.KeyboardButton("Вторник - (10)")
	third_day_ten = types.KeyboardButton("Среда - (10)")
	fourth_day_ten = types.KeyboardButton("Четверг - (10)")
	fifth_day_ten = types.KeyboardButton("Пятница - (10)")
	returning_ten = types.KeyboardButton("Назад к классам")

	#Подключение клавиатуры
	markup_days_for_ten.row(first_day_ten)
	markup_days_for_ten.add(secound_day_ten, third_day_ten, fourth_day_ten, fifth_day_ten)
	markup_days_for_ten.row(returning_ten)

	bot.send_message(message.chat.id, "Выберите день недели: ", reply_markup = markup_days_for_ten)

@bot.message_handler(func=lambda m: m.text=='Понедельник - (10)', content_types=['text'])
def ponedelnik(message):
	bot.send_message(message.chat.id, "1) -\n2) Хімія\n3) Хімія\n4) Історія\n5) Зарубіжна література\n6) Мистецтво\n7) Історія\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Вторник - (10)', content_types=['text'])
def vtornik(message):
	bot.send_message(message.chat.id, "1) Математика\n2) Математика\n3) Захист України\n4) Захист України\n5) Українська література\n6) Українська література\n7) Фізкультура\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Среда - (10)', content_types=['text'])
def sreda(message):
	bot.send_message(message.chat.id, "1) Фізкультура\n2) Фізика\n3) Англійська мова\n4) Англійська мова\n5) Історія\n6) Інформатика\n7) Інформатика\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Четверг - (10)', content_types=['text'])
def chetverg(message):
	bot.send_message(message.chat.id, "1) Математика\n2) Математика\n3) Українська мова\n4) Українська мова\n5) Громадянська освіта\n6) Громадянська освіта\n\n6 уроків")


@bot.message_handler(func=lambda m: m.text=='Пятница - (10)', content_types=['text'])
def pyatnica(message):
	bot.send_message(message.chat.id, "1) Біологія\n2) Біологія\n3) Фізкультура\n4) Географія\n5) Географія\n6) Фізика\n7) Фізика\n\n7 уроків")


@bot.message_handler(func=lambda m: m.text=='Назад к классам', content_types=['text'])
def pyatnica(message):
	bot.send_message(message.chat.id, "Возвращаемся...")
	timetable(message)




@bot.message_handler(func=lambda m: m.text=='Назад к функциям', content_types=['text'])
def nineA_class(message):
	bot.send_message(message.chat.id, "Возвращаемся...")
	welcome(message)




bot.polling(none_stop = True)
