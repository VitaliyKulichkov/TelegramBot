from bs4 import BeautifulSoup as BS
import requests


#Получение данных о погоде
r = requests.get('https://sinoptik.ua/погода-москва')
html = BS(r.content, 'html.parser')


for el in html.select('#content'):
	t_min = el.select('.temperature .min')[0].text
	t_max = el.select('.temperature .max')[0].text
	text = el.select('.wDescription .description')[0].text
