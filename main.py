from Modelos.Restaurante import Restaurante
from Modelos.Cardapio.bebida import Bebida
from Modelos.Cardapio.prato import Prato

PizzaB = Restaurante('Pizt', 'Pizzaria')
PizzaB.receber_avaliacao("henri",5)
PizzaB.receber_avaliacao("henri",4)
Suco = Bebida("Suco Melancia", 5.0,"Grande")
Pao = Prato("Pao", 2.0, "Pao frances")

Suco.aplicar_desconto()
Pao.aplicar_desconto()

PizzaB.adicionar_item_no_cardapio(Pao)
PizzaB.adicionar_item_no_cardapio(Suco)

def main():
    
    Restaurante.listar_restaurantes()
    print()
    PizzaB.listar_cardapio

if __name__ == '__main__':
    main()