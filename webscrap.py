import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome("C:/Downloads/chromedriver")


products=[] 
prices=[]
ratings=[]

driver .get("https://www.flipkart.com/search?q=ac+1.5+ton&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_2_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_3_2_na_na_ps&as-pos=3&as-type=RECENT&suggestionId=ac+1.5+ton&requestId=25a6317f-8677-4ec1-b5d1-12646e48dec4&as-searchtext=ac")

content = driver.page_source
soup = BeautifulSoup(content, features="lxml")

for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    print(products.append(name.text.strip()))
    print(prices.append(price.text.strip()))
    print(ratings.append(rating.text.strip())) 
    print()
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

