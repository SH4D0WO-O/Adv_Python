import requests
import bs4

list = {}
title_list = []
currency_list = []
url = "https://karnameh.com/car-price"

reponse = requests.get(url)

soup = bs4.BeautifulSoup(reponse.text,'html.parser')
title = soup.find_all("div",attrs={"class": "MuiStack-root muirtl-k3jn5p"})
currency = soup.find_all("p", attrs = {"class": "MuiTypography-root MuiTypography-body1 muirtl-22intj"})

for i in title:
    print(i.text)
    #x = (i.text)
    title_list.append(i.text)

for n in currency:
    print(n.text)
    currency_list.append(n.text)

for i in range(len(title_list)):
    list[title_list[i]] = currency_list[1]    

print(title_list)
print(currency_list)
print(list)