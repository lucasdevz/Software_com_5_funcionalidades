import os
os.system("cls || clear")

#Lista de livros
livros = []

#Funçoes das funcionalidades do app
def exibir_nome_do_programa():
    print("""
🇧🇮🇧🇱🇮🇴🇹🇪🇨🇦 🇸🇪🇳🇦🇮
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