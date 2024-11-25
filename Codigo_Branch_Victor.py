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