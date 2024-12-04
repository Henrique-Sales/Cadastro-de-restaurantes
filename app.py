from fastapi import FastAPI, Query
import requests
import json

app = FastAPI()

@app.get('/api/hello')

def hello():
    '''
    Endpoint que retorna mensagem "Hello World" 
    
    '''
    return {'Hello': 'world'}

@app.get('/api/restaurantes/')

def get_restaurantes(restaurante: str = Query(None)):

    '''
    Endpoint para ver cardápio de restaurantes
    '''


    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

    response = requests.get(url=url)

    if response.status_code == 200:
        response_dados = response.json()
        
        dados_restaurante = []
        if restaurante is None:
            return {'Dados':response_dados}
        
        for item in response_dados:
         
            if item['Company'] == restaurante:
                              
                dados_restaurante.append({
                    "item": item['Item'],
                    "price":item['price'],
                    "description": item['description']
                })

        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro':f'{response.status_code} - {response.text}'}
    
    # for nome_do_restatante, dados in dados_restaurante.items():
    #     nome_do_arquivo = f'{nome_do_restatante}.json'
    #     with open(nome_do_arquivo,'w' ) as arquivo_restaurante:
    #         json.dump(dados, arquivo_restaurante, indent=4)
