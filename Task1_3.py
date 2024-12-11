import requests
import bs4

list = {}
N_list = []
R_list = []
url = "https://takhfifan.com/tehran/restaurants-cafes"

reponse = requests.get(url)


soup = bs4.BeautifulSoup(reponse.text,'html.parser')
title = soup.find_all("p",attrs={"class": "vendor-card-box__title-text"})
rate = soup.find_all("p", attrs = {"class" : "rate-badge__rate-value"})

for i in title:
    print(i.text)
    N_list.append(i.text)

for i in rate:
    print(i.text)
    R_list.append(i.text)
    
for i in range(len(N_list)):
    list[N_list[i]] = R_list[i]

N_list = sorted(list.items() , key=lambda x: x[1], reverse = True)
f_list = dict(N_list)
    
#print(N_list)
#print(R_list)
print(f_list)