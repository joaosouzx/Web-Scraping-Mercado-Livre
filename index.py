import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Insira a categoria desejada:")
x = input()

# URL da página a ser analisada
url = "https://lista.mercadolivre.com.br/"+x+"#D[A:"+x+"]"

# Faz a requisição GET na URL e armazena o conteúdo em uma variável
response = requests.get(url)

# Cria um objeto BeautifulSoup a partir do conteúdo da página
soup = BeautifulSoup(response.content, 'html.parser')

# Cria as listas que irão armazenar os dados dos produtos
titles = []
prices = []

# Encontra todas as tags <div> com a classe "ui-search-result__content-wrapper"
product_containers = soup.find_all('div', {'class': 'ui-search-result__content-wrapper'})

# Extrai o título e o preço de cada produto
for container in product_containers:
    # Extrai o título do produto
    title_element = container.find('h2', {'class': 'ui-search-item__title'})
    if title_element:
        title = title_element.text.strip()
    else:
        title = "N/A"

    # Extrai o preço do produto
    price_element = container.find('span', {'class': 'price-tag-fraction'})
    cents_element = container.find('span', {'class': 'price-tag-cents'})
    if price_element and cents_element:
        price = price_element.text.strip() + '.'+ cents_element.text.strip()
    elif price_element:
        price = price_element.text.strip() + '.00'
    else:
        price = "N/A"

     # Adiciona o título e o preço do produto às listas
    titles.append(title)
    prices.append(float(price))

# Cria um DataFrame pandas a partir das listas de títulos e preços
df = pd.DataFrame({'Nome': titles, 'Preço': prices})

# Ordena o DataFrame pelo preço em ordem decrescente
df = df.sort_values('Preço', ascending=False)

# Imprime o DataFrame na tela
print(df.to_string(index=False))
