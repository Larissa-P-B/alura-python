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

print(dados_res['McDonald’s'])    
