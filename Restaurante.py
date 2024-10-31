import os
import time

restaurantes = [

    {"Nome":"Sabores", "Categoria":"Italiano", "Status":False},
    {"Nome":"Pitz", "Categoria":"Pizzaria", "Status":True}

]



def pesquisar_restaurante(nome):

    encontrado = False

    for restaurante in restaurantes:

        if restaurante['Nome'] == nome:
            encontrado = True
    return encontrado


def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():

    ''' Função responsável por exibir lista de opções '''

    print("1. Cadastrar Restaurantes")
    print("2. Listar Restaurantes")
    print("3. Alterar status de Restaurantes")
    print("4. Sair")

def escolher_opcao():
    try:
        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            cadastar_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            ativar_restaurante()

        elif opcao == 4:
            exibir_subtitulo("Saindo")
            time.sleep(1.5)
            os.system('cls')
    except:
        print("\nOpção inválida\n")
        input("Pressione uma tecla para voltar ao menu principal: ")
        main()

def voltar_ao_menu():
    input("\nPressione uma tecla para voltar ao menu principal: ")

    main()

def listar_restaurantes():

    ''' Função responsável por exibir lista de restaurantes'''

    print("\n")
    exibir_subtitulo("Listando restaurantes")

    print(f"{'Nome do restaurante'.ljust(20)} | {'Status'.ljust(20)}")
    for restaurante in restaurantes:
        nome = restaurante['Nome']
        ativo = "Ativo" if restaurante['Status'] else "Desativado"
        print(f"{nome.ljust(20)} | {ativo.ljust(20)}")
    voltar_ao_menu()    

def cadastar_restaurante():

    ''' Função responsável por cadastrar novos restaurantes.

    Inputs:
    - Nome do Restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes.
    '''

    exibir_subtitulo("Cadastro de restaurantes")
    nome = input("Digite o nome do restaurante: ")
    categoria = input("Digite a categoria do restaurante: ")

    cadastro = {"Nome":nome, "Categoria":categoria, "Status":False}
    restaurantes.append(cadastro)

    print(f"Restaurante {nome} cadastrado com sucesso!")
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    caratere ='*'
    tamanho = len(texto)+4
    print(caratere*tamanho)
    print(f"* {texto} *")
    print(caratere*tamanho)
    print()


def ativar_restaurante():
    exibir_subtitulo("Alterar status de Restaurante")

    nome = input("Digite o nome do restaurante: ")
    pesquisa = pesquisar_restaurante(nome)

    if pesquisa:
        
        for restaurante in restaurantes:
            if restaurante['Nome'] == nome:
                restaurante['Status'] = not restaurante["Status"]
                match restaurante["Status"]:
                    case True:
                        print(f"Restaurante {nome} ativado com sucesso!")
                    case False:
                        print(f"Restaurante {nome} desativado com sucesso!")
                
        voltar_ao_menu()
    else:
        print(f"Restaurante {nome} não encontrado")
        time.sleep(1,5)
        voltar_ao_menu()
        
def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()



if __name__ == '__main__':
    main()

