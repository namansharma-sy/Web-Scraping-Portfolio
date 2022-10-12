from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import json

stockList = []

def getData(symbol):
    url = f'https://finance.yahoo.com/quote/{symbol}'

    driver = webdriver.Chrome()
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source)
    
    price = soup.find(class_ = 'Fw(b) Fz(36px) Mb(-4px) D(ib)').text
    diff = soup.find('div', class_ = 'D(ib) Mend(20px)').find_all('span')[0].text 
    percnt = soup.find('div', class_ = 'D(ib) Mend(20px)').find_all('span')[1].text
    change = f'{diff} + {percnt}'

    
    stock = {
        "symbol" : symbol,
        "price" : price,
        "diff" : diff,
        "percnt" : percnt,
        "change" : f'{diff} + {percnt}'
    }
    return stock

myStock = ['GOOGL-USD', 'FB-USD', 'DPI-USD', 'GHST-USD', 'TSLA', 'ARKX', 'LYFT', 'UBER',\
          'ABNB', 'DASH', 'SNAP', 'TWTR', 'META']

for stock in myStock:
    stockList.append(getData(stock))
    
with open('stockData.json', 'w') as f:
    json.dump(stockList, f)