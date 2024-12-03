from Modelos.avaliacao import Avaliacao
from Modelos.Cardapio.item_cardapio import ItemCardapio

class Restaurante:
    Restaurantes = []
    def __init__(self,nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._status = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.Restaurantes.append(self)

    def __str__(self) -> str:
        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'.ljust(20)}')
        for restaurante in cls.Restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.media_avaliacao.ljust(20)} | {restaurante.status.ljust(20)}' )

    @property
    def status(self):
        return '✅ Ativo 'if self._status else '❌ Desativado'

    def alternar_estado(self):
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):

        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            print('Avalição não realizada, informe uma nota de 0 a 5')
    @property    
    def media_avaliacao(self):
        if len(self._avaliacao) == 0:
            return '-'
        else:
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)

            quantidade_de_avaliacoes = len(self._avaliacao)

            media = round(soma_das_notas/quantidade_de_avaliacoes,1)


            return str(media)


    def adicionar_item_no_cardapio(self, item):

        if  isinstance(item, ItemCardapio):
            self._cardapio.append(item)    

    @property
    def listar_cardapio(self):
        print(f"Cardápio do restaurante {self._nome} \n")
        print()
        for i, item in enumerate(self._cardapio, start=1):
     
            if hasattr(item, '_tamanho'):
                
                print(f'{i}. - Nome: {item._nome.ljust(20)} | Preço: R$ {str(item._preco).ljust(20)} | Tamanho: {item._tamanho.ljust(20)}')
            else:
                print(f'{i}. - Nome: {item._nome.ljust(20)} | Preço: R$ {str(item._preco).ljust(20)} | Descrição : {item._descricao.ljust(20)}')


