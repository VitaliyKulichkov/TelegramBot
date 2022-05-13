from bs4 import BeautifulSoup as BS
import requests



responce = requests.get('https://www.banki.ru/products/currency/cash/moskva/')
html = responce.text
soup = BS(html, 'html.parser')


exchange_rates = soup.findAll('div', {'class':'table-flex__cell table-flex__cell--without-padding padding-left-default'})
word = (exchange_rates[0].text)
usd = (exchange_rates[1].text)
eur = (exchange_rates[2].text)
