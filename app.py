import os

lista_de_restaurante = []


def iniciar_app():
    '''
    Exibe o nome estilizado do programa na tela
    '''
    print('__ CATÁLOGO DE RESTAURANTES __')


def exibir_subtitle(txt):
    '''
    Exibe um subtítulo estilizado na tela 
    
    Inputs:
    texto: str - O texto do subtítulo
    '''
    os.system('cls')
    print(f'__ {txt} __')


def exibir_opcoes():
    '''
    Exibe as opções disponíveis no menu principal
    '''
    print('''
    1- Cadastra Restaurante
    2- Listar Restaurante
    3- Ativar Restaurante
    4- Sair
      ''')


def esconher_opcao():
    '''
    Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Voçê escolheu a opção {opcao_escolhida}.')

        if opcao_escolhida == 1:
            cadastrando_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            ativar_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()
        
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def retorna_ao_menu():
    '''
    Solicita uma tecla para voltar ao menu principal

    Outputs:
    Retorna ao menu principal
    '''
    input('\nEnter para retornar ')  
    main()


def cadastrando_restaurante():
    '''
    Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitle('Cadastro de Restaurantes')

    nome_restaurante = str(input('Nome do Restaurante: ')).title()  #  obter nome do restaurante
    categoria_restaurante = str(input('Informe a categoria: ')).title()  # obter categorio, e ativo/False
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}  # adc nome, categoria, ativo a variavel deir dados
    lista_de_restaurante.append(dados_restaurante)  # adc todos os dados a lista

    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    retorna_ao_menu()


def listar_restaurantes():
    '''
    Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tel
    '''
    exibir_subtitle('Lista de Restaurantes')

    if len(lista_de_restaurante) < 1:  #doc string
        print('Lista de Restaurantes "vazia"')
        retorna_ao_menu()

    else:
        for restaurante in lista_de_restaurante:  # pecorre cada alemento da lista para listar e apresentar
            status = f'Ativo' if restaurante['ativo'] else f'Desativado'  # mudar a forma de apresenta o status False=Desativado True=ativo
            print(f'{restaurante['nome']} | {restaurante['categoria']} | {status}')  # aprensenta a lista formatada        

        retorna_ao_menu()


def ativar_restaurante():
    '''
    Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação

    '''
    exibir_subtitle('Alternar Estado')

    nome_restaurante = str(input('Informe o restaurante para alterar o estado: ')).title()
    restaurante_encontrado = False

    for restaurante in lista_de_restaurante:
        if nome_restaurante == restaurante['nome']: # nome informado encontra-se na lista
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']  # nessa linha, a variavel recebe o inverso dela, se for False passa para True vice-versa
            menssagem = f'O restaurante {nome_restaurante} foi ativado' if restaurante['ativo'] else f'O Restaurante {nome_restaurante} foi desativado'
            print(menssagem)

    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante}  não encontrado')

    retorna_ao_menu()


def opcao_invalida():
    '''
    Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    exibir_subtitle('Opção invalida')
    retorna_ao_menu()


def finalizar_app():
    '''
    Exibe mensagem de finalização do aplicativo
    '''
    exibir_subtitle('Volte Sempre!')
    print(f'Finalizando o app...')


def main():
    '''
    Função principal que inicia o programa
    '''
    os.system('cls')
    iniciar_app()
    exibir_opcoes()
    esconher_opcao()
            

if __name__ == '__main__':
    main()