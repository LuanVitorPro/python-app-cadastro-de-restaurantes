import os

restaurantes = [{'nome':'Praça', 'categoria': 'cafés', 'ativo':False },
                {'nome':'pizza pizzuda', 'categoria':'pizzas', 'ativo': True},
                {'nome': 'frangolinos', 'categoria':'carnes', 'ativo': False}]

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
    '''Exibe as opções ao usuario'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''Usa um retorno do usuario (input) para voltar ao inicio'''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida(): 
    '''Em caso do usuario digitar algum caractere invalido'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Exibe o subtitulo de cada ação escolhida pelo usuario
    
    exibe bordar (linha)ao redor dos subtitulos tambem'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Função para cadastrar restaurantes, pedindo ao usuarios informaçoes
    de nome e categoria.
   
   inputs: nome_do_restaurante e categoria

    
    Output: E por final adiciona a lista de restaurantes do app'''
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Qual será a categoria do restaurante {nome_do_restaurante}? ')
    
    dados_do_restaurante = {'nome':nome_do_restaurante, 
                            'categoria':categoria, 
                            'ativo':False }
    
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Lista todos os restaurantes cadastrados exibindo: nome, categoria e
    se está ativo ou desativado.

    Ele altera o nome de false ou true para ativo ou desatidado do estado 
    do restaurente para melhora o entendimento do usuario.   
    '''
    exibir_subtitulo('Listando restaurantes')
    print(f"{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}")
    print('-' * 60)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurente = restaurante['categoria']
        ativo_restaurante = restaurante['ativo']
        status = 'ativado' if ativo_restaurante else 'desativado'
        print(f' -{nome_restaurante.ljust(20)}  | {categoria_restaurente.ljust(20)} | {status.ljust(20)}')

    voltar_ao_menu_principal()

def alterar_estado_do_restaurante():
    '''Esse funçao altera o estado do restaurante de ativo e desativado.
    
    Quando o usuario digita o nome do estraurante no input e o restaurante
    é encontrado, a funçao faz a troca do estado, se tiver ativado ele 
    desativa e vice versa.
    
    caso a erro na digitaçao ele avisa que teve erro ao encontrar'''
    exibir_subtitulo('Alterando o estado do restaurante.')
    nome_restaurante = input('Digite o nome do restaurante que deseja fazer a alteração: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
        estado_restaurante = 'ativo' if restaurante['ativo'] else 'desativado'
        restaurante['ativo'] = not estado_restaurante
        mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
        print(mensagem)
        break

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')
    
    voltar_ao_menu_principal()


def escolher_opcao():
    '''registra o input do usuario ao escolher uma funçao e direciona para
    a mesma. 
    ex: se a opçao escolhida for 1, ira cadastrar novo restaurante
    
    A opçao_invalida é caso não tenha sido digitada nenhum das teclas
    correspondentes as opçoes(1.2.3.4)'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alterar_estado_do_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Junta as quatro funcoes para limpar e restabelecer o menu de opções
    ao usuario novamente'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()