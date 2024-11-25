

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