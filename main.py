from Modelos.Restaurante import Restaurante
from Modelos.Cardapio.bebida import Bebida
from Modelos.Cardapio.prato import Prato


PizzaB = Restaurante('Pizt', 'Pizzaria')

Suco = Bebida("Suco Melancia", 5.0, "Grande")
Pao = Prato("Pao", 2.0, "Pao frances")

PizzaB.adicionar_bebida_no_cardapio(Pao)
PizzaB.adicionar_bebida_no_cardapio(Suco)

def main():
    PizzaB.listar_cardapio




if __name__ == '__main__':
    main()