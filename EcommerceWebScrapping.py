from bs4 import BeautifulSoup
import requests 
import pandas as pd


linkList = []

def getData():
    
    for page in range(1,5):
        url = f'https://www.thewhiskyexchange.com/search?q=japanese+wiskey&pg={page}'

        source = requests.get(url)
        soup = BeautifulSoup(source.text)

        items = soup.find_all('a', class_ = "product-card")

        for item in items:
            linkList.append('https://www.thewhiskyexchange.com'+item['href'])

    wiskey = {}
    wiskeyList = []
    #url = 'https://www.thewhiskyexchange.com/p/32761/yoichi-single-malt'

    for link in linkList:

        source = requests.get(link)
        soup = BeautifulSoup(source.text)   


        name = soup.find("h1", class_ = 'product-main__name').text.strip()
        try:
            fulfilment = soup.find("div", class_ = 'review-overview').text.strip()
            rating = fulfilment.split('\n')[0]
            review = fulfilment.split('\n')[-1].replace('\xa0Reviews',"")[1:-1]
        except:
            rating = 'No rating'
            review = 'No Reviews'

        price = soup.find("p", class_ = 'product-action__price').text


        wiskey = {
            'Name' : name,
            'Rating' : rating,
            'Review' : review,
            'Price' : price
        }
        wiskeyList.append(wiskey)

    df = pd.DataFrame(wiskeyList)
    return df.to_csv("wiskeyList.csv")

getData()