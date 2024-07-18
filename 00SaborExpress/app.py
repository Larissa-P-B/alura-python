import json
import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
print(response)

if response.status_code == 200: 
    dados_json = response.json()
    dados_res = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_res:
            dados_res[nome_restaurante] = []

        dados_res[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "descricao": item['description']
        })    
else:
    print(f'O erro foi {response.status_code}')  

for nome_restaurante, dados in dados_res.items():
    nome_do_arquivo = f'{nome_restaurante}.json'
    with open(nome_do_arquivo, 'w') as aqr_res:
        json.dump(dados,aqr_res,indent=4)

