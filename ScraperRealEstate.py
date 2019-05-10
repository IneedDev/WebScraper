import requests
import pip
from bs4 import BeautifulSoup
#How to define list of x elements create variable 'location' and add this var as url sufix
print("Average real-estate price based on data from www.gumtree.pl")
start = input("Start: Y/N: ")
room = input("Number of rooms: (1,2,3,4) ")
miasto = input("City (Krakow, Warszawa, Katowice): ")
dzielnica = str(input("District (Nowa Huta, Bronowice, Śródmieście, Prądnik): "))
if miasto == '':
    print("Podaj nazwę miasta")
    miasto = input("City (Krakow, Warszawa, Katowice): ")
elif miasto == 'Warszawa':
    name = 'warszawa'
print("It will take a while...")
for strona in range(2, 5):
    page = requests.get('https://www.gumtree.pl/s-mieszkania-i-domy-sprzedam-i-kupie/krakow/mieszkanie/page-' + str(strona) + '/v1c9073l3200208q0p' + str(strona) + '?nr=' + str(room) + '&priceType=fixed')
    #'https://www.gumtree.pl/s-mieszkania-i-domy-sprzedam-i-kupie/'+ str(name) + '/mieszkanie/page-'+ str(strona) + '/v1c9073l3200208q0a1dwp' + str(strona) + '?nr='+str(room)+'&priceType=fixed')
    #https://www.gumtree.pl/s-mieszkania-i-domy-sprzedam-i-kupie/krakow/nowa+huta/v1c9073l3200208q0p1?nr=2&priceType=fixed
    soup = BeautifulSoup(page.text, 'html.parser')
    price = soup.find('span', class_='amount')
    price_list = soup.find_all('span', class_='amount')
    description_list = soup.find_all('a', class_='href-link')
    #print(page.url)
lista = []
for price_list_items in price_list:
    for values in price_list_items:
        x= values.rstrip(' zł')
        lista.append(x)
        print(values)
for idx, item in enumerate(lista):
            item = item.split()
            item = ''.join(item)
            lista[idx] = int(item)
print(lista)
suma = sum(lista)
lenght = len(lista)
print(lenght)
srednia = suma / lenght
cenasrednia = round(srednia, 3)
print("Średnia cena sprzedaży mieszkania " + str(room) + "-pokojowego w mieście " + str(miasto) + " wynosi: " + str(cenasrednia) + " zł")
print("Dane zebrane na podstawie:" + str(lenght) + " ogłoszeń")














