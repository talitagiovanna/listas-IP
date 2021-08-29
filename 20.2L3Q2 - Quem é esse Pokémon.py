#quantidade pokémons que serão fornecidos
N = int(input())

#lista com os nomes dos pokémons e seus respectivos elementos
pokemon_elemento = []

#inserir os nomes dos pokémons e seus respectivos elementos
for i in range(N):
    pokemon_elemento.append(input().split())

while True:
    #pesquisa pelo nome do Pokemon
    pesquisa = input()
    #para saber se faz a pesquisa por nome do pokemon ou elemento
    if pesquisa == 'Pokemon':
        nome_pokemon = input()
        tem_pokemon = False
        elemento = ''
        quantidade_elemento = 0
        #busca do pokemon na lista
        for pokemon in pokemon_elemento:
            var = pokemon[0]
            if var == nome_pokemon:
                tem_pokemon = True
                elemento = pokemon[1]
        #quando tem pokemon
        if tem_pokemon:
            for elementos in pokemon_elemento:
                elementos = elementos[1]
                if elementos == elemento:
                    quantidade_elemento += 1
        #quando não tem pokemon
        if not tem_pokemon:
            print(f"Não existe o pokemon {nome_pokemon} na PokeDex")
        elif quantidade_elemento > 0:
            print(f"O pokemon {nome_pokemon} tem o elemento {elemento}. E existem {quantidade_elemento} pokemons do elemento {elemento}")
    #pesquisa pelo elemento do pokemon
    elif pesquisa == 'Elemento':
        elemento_pesquisado = input()
        tem_elemento = False
        a = ''
        #busca do elemento na lista
        for elem in pokemon_elemento:
            elem = elem[1]
            if elem == elemento_pesquisado:
                tem_elemento = True
                a = elem
        #quando tem o elemento na lista
        if tem_elemento:
            pokemon_elementos = []
            for el in pokemon_elemento:
                poke = el[0]
                el = el[1]
                if el == a:
                    pokemon_elementos.append(poke)
            print("Os pokemons da PokeDex que tem esse mesmos elemento e/são:")
            print(f"{' '.join(pokemon_elementos)}")
        #quando não tem o elemento na lista
        if not tem_elemento:
            print(f"Não existe nenhum pokemon na PokeDex com o elemento {elemento_pesquisado}")
    #quando o comando é diferente de pokemon e elemento
    else:
        print("Comando diferente de Pokemon ou Elemento. Programa encerrado!")
        break