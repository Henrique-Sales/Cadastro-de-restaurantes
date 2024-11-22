from Modelos.avaliacao import Avaliacao


class Restaurante:
    Restaurantes = []
    def __init__(self,nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._status = False
        self._avaliacao = []
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
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property    
    def media_avaliacao(self):
        if self._avaliacao == 0 or len(self._avaliacao) == 0:
            return str(0)
        else:
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)

            quantidade_de_avaliacoes = len(self._avaliacao)

            media = round(soma_das_notas/quantidade_de_avaliacoes,1)


            return str(media)




        