from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd

# url of all addresses
url = "https://www.enterprise.com/en/car-rental-locations.html?icid=header.locations.car.locations-_-international.locations-_-ENUS.NULL"


# lables=pd.read_html(url)
# print(lables)

# setting up the right header 
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}

r= requests.get(url,headers=headers)
soup = bs(r.content,"html.parser")
print(soup)