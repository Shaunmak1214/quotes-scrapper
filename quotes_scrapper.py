from bs4 import BeautifulSoup
import requests

def spacequotes():
    quotesArr = []
    space_quotes = requests.get('https://www.brainyquote.com/topics/space-quotes').text
    soup = BeautifulSoup(space_quotes, 'lxml')
    quotes = soup.find_all('a', {'title' : 'view quote'})

    for idx, item in enumerate(quotes):
        itemsByNum = item.text
        quotesArr.append(itemsByNum)

    return quotesArr

def spacequotes1():
    quotesArr = []
    space_quotes = requests.get('http://www.notable-quotes.com/s/space_travel_quotes.html').text
    soup = BeautifulSoup(space_quotes, 'lxml')
    quotes = soup.find_all('p', class_ = "quotation")

    for idx, item in enumerate(quotes):
        itemsByNum = item.text
        quotesArr.append(itemsByNum)

    return quotesArr


""" response = spacequotes1();
print (response) """

