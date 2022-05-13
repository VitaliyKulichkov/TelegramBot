import config
import telebot
from telebot import types
from googletrans import Translator
import random
import ExchangeRate
import Weather
import pyjokes

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands = ['start'])
def main(message):
	bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user) + '\nВоспользуйся коммандой /nav или /menu для открытия меню' + '\nТакже ты можешь воспользоваться командой /help для получения справки')

@bot.message_handler(commands = ['help'])
def get_info(message):
	bot.send_message(message.chat.id, '/start -> начало работы с ботом\n /help -> данное сообщение\n /nav или /menu -> открытие меню')

@bot.message_handler(commands= ['nav', 'menu'])
def navigation(message):
	nav = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton('Погода')
	item2 = types.KeyboardButton('Рандомное число')
	item3 = types.KeyboardButton('Шутки')
	item4 = types.KeyboardButton('Курс валюты')
	nav.add(item1, item2, item3, item4)
	bot.send_message(message.chat.id, 'Выбери пункт меню, который тебя интересует', reply_markup=nav)

@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.chat.type == 'private':
		if message.text == 'Рандомное число':
			bot.send_message(message.chat.id, 'Ваше число =' + ' ' + str(random.randint(0,1000)))
		elif message.text == 'Погода':
			bot.send_message(message.chat.id, Weather.text + '\nТемпература: ' + Weather.t_min + ',' + Weather.t_max)
		elif message.text == 'Курс валюты':
			nav = types.ReplyKeyboardMarkup(resize_keyboard=True)
			it1 = types.KeyboardButton("Курс Доллара")
			it2 = types.KeyboardButton("Курс Евро")
			back = types.KeyboardButton('Назад')
			nav.add(it1, it2, back)
			bot.send_message(message.chat.id, 'Курсы валюты', reply_markup=nav)
		elif message.text == 'Шутки':
			nav = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('Шутка')
			item2 = types.KeyboardButton('Назад')
			nav.add(item1, item2)
			bot.send_message(message.chat.id, 'Быстрее жми на кнопку, чтобы получить шутку', reply_markup=nav)
		elif message.text =='Шутка':
			joke = pyjokes.get_joke(language='en', category='all')
			translator = Translator()
			joke_translated = translator.translate(joke, dest='ru')
			bot.send_message(message.chat.id, joke_translated.text)
		elif message.text == 'Курс Доллара':
			bot.send_message(message.chat.id, ExchangeRate.word + " = " + ExchangeRate.usd + "руб.")
		elif message.text == 'Курс Евро':
			bot.send_message(message.chat.id, ExchangeRate.word + " = " + ExchangeRate.eur + "руб.")
		elif message.text == 'Назад':
			nav = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('Погода')
			item2 = types.KeyboardButton('Рандомное число')
			item3 = types.KeyboardButton('Шутки')
			item4 = types.KeyboardButton('Курс валюты')
			nav.add(item1, item2, item3, item4)
			bot.send_message(message.chat.id, 'Назад', reply_markup=nav)

if __name__ == '__main__':
	bot.polling(none_stop=True)



