import requests
import bs4

url = "https://tv.filmnet.ir"

reponse = requests.get(url)

soup = bs4.BeautifulSoup(reponse.text,'html.parser')
title = soup.find_all("div",attrs={"class":"css-1wmimpn eofezqb0"})

for i in title:
    print(i.text)