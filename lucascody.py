import os
os.system('cls')

livros = ['Harry Potter', 'Damon Slayer']

def exibir_nome_do_programa():
    print("""
🇧​​​​​🇮​​​​​🇧​​​​​🇱​​​​​🇮​​​​​🇴​​​​​🇹​​​​​🇪​​​​​🇨​​​​​🇦​​​​​ 🇸​​​​​🇪​​​​​🇳​​​​​🇦​​​​​🇮​​​​​
""")

def exibir_opcoes():
    print('1. Cadastrar Livros')
    print('2. Listar Livros')
    print('3. xxxxxxxxxxxx')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
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

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_livro()
        elif opcao_escolhida == 2: 
            listar_livros()
        elif opcao_escolhida == 3: 
            print('xxxxxxxxx')
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()