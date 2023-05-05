import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL da página de pesquisa
url = "https://lista.mercadolivre.com.br/suculenta#D[A:suculenta]"

# fazer a requisição HTTP
response = requests.get(url)

# extrair o HTML da página
html = response.content

# criar o objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# extrair as informações de título e preço dos produtos
titles = [title.text.strip() for title in soup.find_all("span", class_="main-title")]
prices = [float(price.text.strip("R$ ").replace(",", ".")) for price in soup.find_all("span", class_="price__fraction")]

# criar um DataFrame com os dados extraídos
data = pd.DataFrame({"Title": titles, "Price": prices})

# ordenar os dados pelo preço em ordem decrescente
data = data.sort_values("Price", ascending=False)

# formatar a coluna de preços como moeda
data["Price"] = data["Price"].apply(lambda x: f"R$ {x:.2f}")

# exibir a tabela no terminal
print(data.to_string(index=False, justify="center"))
