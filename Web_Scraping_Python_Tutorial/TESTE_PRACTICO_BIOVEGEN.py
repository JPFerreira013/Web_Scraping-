
import requests

from bs4 import BeautifulSoup

import csv
#Make a request

page = requests.get('https://biovegen.org/category/socios/')

#Testando para ver se a requicao funcionou 
#print(page)

soup = BeautifulSoup(page.content, 'html.parser')

# Create all_products as empty list
all_empresas = []

empresas = soup.select('div.text-center.d-table-row')

for elementos in empresas:
    name = elementos.select('h5 > a.title')[0].text.strip()
    area_enfoque = elementos.select('p.post-excerpt.small')[0].text.strip()

    info = {
        "name": name,
        "area_enfoque": area_enfoque
    }

    all_empresas.append(info)

print(all_empresas)

keys = all_empresas[0].keys()

with open('empresas.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_empresas)
