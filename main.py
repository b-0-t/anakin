from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd

# url for getting all countries
url_countries = "https://www.enterprise.com/en/car-rental-locations.html?icid=header.locations.car.locations-_-international.locations-_-ENUS.NULL"

# setting up the right header to avoid blocking
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}

r= requests.get(url_countries,headers=header)

if(r.status_code==200):
    soup = bs(r.content,"html.parser")
    # print(soup)
else:
    print("Failed to fetch page")



divs_with_countryList = soup.find_all('div',class_='list link-list-band--4-column aem-GridColumn aem-GridColumn--default--12')

countries=[]
for spans in range(1,len(divs_with_countryList)):
    countries+=[country.text for country in divs_with_countryList[spans].find_all('span')]



print(countries)