import os

restaurantes = [{'nome':'Praça', 'categoria': 'japonesa','ativo':False},
                 {'nome':'Pizza Suprema', 'categoria': 'Pizza','ativo':True},
                 {'nome':'Cantina', 'categoria': 'italiana','ativo':False}]

def exibir_nome_programa():
    print("""
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
      """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Encerrando o APP')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto)) 
    print(linha)   
    print(texto)
    print(linha)

def opcao_invalida():
     print('Opção invalida\n')
     voltar_ao_menu()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel  por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Add um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante,
    'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu()

def listar_restaurantes():

    exibir_subtitulo('Listando Restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for r in restaurantes:
        nome_restaurante = r['nome']
        categoria = r['categoria']
        ativo = 'ativado' if r['ativo']else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for r in restaurantes:
        if nome_restaurante == r['nome']:
            restaurante_encontrado = True
            r['ativo'] = not r['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso! 'if r['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso! '
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')        

    voltar_ao_menu()        


def escolher_opcao(): 
    try:   
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2 :
            listar_restaurantes() 
        elif opcao_escolhida == 3 :
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()     
        else :
            opcao_invalida()   
    except:
        opcao_invalida()        

def main():
     os.system('cls')
     exibir_nome_programa()
     exibir_opcoes()
     escolher_opcao()
    
    
    
if __name__ == '__main__':
        main()    




