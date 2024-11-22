from Modelos.Restaurante import Restaurante


PizzaB = Restaurante('Pizt', 'Pizzaria')
PizzaB.receber_avaliacao("Henri",10)
PizzaB.receber_avaliacao("Henri",9)
PizzaB.receber_avaliacao("Henri",8)

Mexico = Restaurante('Chin sh', 'Chinesa')
Mexico.receber_avaliacao("henrique", 5)
Mexico.receber_avaliacao("julho", 2)

bk = Restaurante('Burguer King', 'Fast-food')

def main():
    Restaurante.listar_restaurantes()



if __name__ == '__main__':
    main()