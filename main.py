from Modelos.Restaurante import Restaurante
from Modelos.Cardapio.bebida import Bebida
from Modelos.Cardapio.prato import Prato
import requests
import json

# PizzaB = Restaurante('Pizt', 'Pizzaria')
# PizzaB.receber_avaliacao("henri",5)
# PizzaB.receber_avaliacao("henri",4)
# Suco = Bebida("Suco Melancia", 5.0,"Grande")
# Pao = Prato("Pao", 2.0, "Pao frances")

# Suco.aplicar_desconto()
# Pao.aplicar_desconto()

# PizzaB.adicionar_item_no_cardapio(Pao)
# PizzaB.adicionar_item_no_cardapio(Suco)

# def main():
    
#     Restaurante.listar_restaurantes()
#     print()
#     PizzaB.listar_cardapio

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url=url)

if response.status_code == 200:
    response = response.json()
    
    dados_restaurante = {}
    for item in response:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
            
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price":item['price'],
            "description": item['description']
        })

for nome_do_restatante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restatante}.json'
    with open(nome_do_arquivo,'w' ) as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
