from bs4 import BeautifulSoup
import requests
import time

# print("Insira a categoria:")
# x = input()
# print("Categoria inserida: " + x)

# html = requests.get("https://shopee.com.br/search?keyword="+x).content
html = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(html, 'html.parser')
# i = soup.find_all(class_='shopee-item-card__hover-footer')

temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

print(temperatura.string)

