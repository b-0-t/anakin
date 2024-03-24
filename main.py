from bs4 import BeautifulSoup as bs
import requests 

url = "https://www.enterprise.com/en/car-rental-locations.html?icid=header.locations.car.locations-_-international.locations-_-ENUS.NULL"


r= requests.get(url)
print(r.content)



