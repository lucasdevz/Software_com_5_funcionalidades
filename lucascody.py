import os
os.system("cls || clear")

#Lista de livros
livros = ['Harry Potter', 'Damon Slayer']

#Funçoes das funcionalidades do app
def exibir_nome_do_programa():
    print("""
🇧​​​​​🇮​​​​​🇧​​​​​🇱​​​​​🇮​​​​​🇴​​​​​🇹​​​​​🇪​​​​​🇨​​​​​🇦​​​​​ 🇸​​​​​🇪​​​​​🇳​​​​​🇦​​​​​🇮​​​​​
""")

def exibir_opcoes():
    print('1. Cadastrar Livros')
    print('2. Listar Livros')
    print('3. Buscar Livro')
    print('4. Remover Livro')
    print('5. Editar Livro')
    print('6. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls || clear')
    print(texto)
    print()

def cadastrar_novo_livro():
    exibir_subtitulo('Cadastro de novos livros')
    nome_do_livro = input('Digite o nome do livro que deseja cadastrar: ')
    livros.append(nome_do_livro)
    print(f'O livro {nome_do_livro} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_livros():
    exibir_subtitulo('Listando livros')

    for livro in livros:
        print(f'.{livro}')

    voltar_ao_menu_principal()

def buscar_livro():
    exibir_subtitulo('Buscar Livro')
    nome_do_livro = input('Digite o nome do livro que deseja buscar: ')
    if nome_do_livro in livros:
        print(f'O livro "{nome_do_livro}" está cadastrado.')
    else:
        print(f'O livro "{nome_do_livro}" não foi encontrado.')
    voltar_ao_menu_principal()

def remover_livro():
    exibir_subtitulo('Remover Livro')
    nome_do_livro = input('Digite o nome do livro que deseja remover: ')
    if nome_do_livro in livros:
        livros.remove(nome_do_livro)
        print(f'O livro "{nome_do_livro}" foi removido com sucesso!')
    else:
        print(f'O livro "{nome_do_livro}" não foi encontrado.')
    voltar_ao_menu_principal()

def editar_livro():
    exibir_subtitulo('Editar Livro')
    nome_do_livro_antigo = input('Digite o nome do livro que deseja editar: ')
    if nome_do_livro_antigo in livros:
        novo_nome_do_livro = input('Digite o novo nome do livro: ')
        index = livros.index(nome_do_livro_antigo)
        livros[index] = novo_nome_do_livro
        print(f'O livro "{nome_do_livro_antigo}" foi atualizado para "{novo_nome_do_livro}".')
    else:
        print(f'O livro "{nome_do_livro_antigo}" não foi encontrado.')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1: 
            cadastrar_novo_livro()
        elif opcao_escolhida == 2: 
            listar_livros()
        elif opcao_escolhida == 3: 
            buscar_livro()
        elif opcao_escolhida == 4: 
            remover_livro()
        elif opcao_escolhida == 5: 
            editar_livro()
        elif opcao_escolhida == 6: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

#Exibindo tudo na funçao principal
def main():
    os.system('cls || clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()