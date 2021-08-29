#lista com o nome dos avatares
avatares = ['Korra da tribo da Água do Sul', 'Aang do Templo do Ar do Sul', 'Roku da Nação do Fogo', 'Kyoshi do Reino da Terra', 'Kuruk da Tribo da Água do Norte', 'Yangchen do Templo do Ar do Oeste', 'Szeto da Nação do Fogo', 'Wan o Primeiro']

#lista de avatares encontrados
avatar_encontrado = []
#verificar se o avatar está na lista de avatares
while True:
    try:
        nome_avatar = input()
        #verificando se o avatar está na lista inicial
        if nome_avatar in avatares:
            if nome_avatar not in avatar_encontrado:
                avatar_encontrado.append(nome_avatar)
    except EOFError:
        if len(avatar_encontrado) > 0:
            print("Os Avatares encontrados foram:")
            print()
            print('\n'.join(avatar_encontrado))
        else:
            print("Nenhum Avatar foi encontrado")
        break