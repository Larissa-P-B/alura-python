from fastapi import FastAPI,Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    ENDPOINT que exibe uma mensagem 

    '''
    return {'Hello': 'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    ENDPOINT para ver os cardapios dos restaurantes 

    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    if response.status_code == 200: 
        dados_json = response.json()
        if restaurante is None:
             return {'Dados': dados_json}
        dados_res = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_res.append({
                "item": item['Item'],
                "price": item['price'],
                "descricao": item['description']
                }) 
        return {'Restaurante': restaurante, 'Cardapio': dados_res}           
    else:
        return {'Erro':f'{response.status_code} - {response.text}' }
