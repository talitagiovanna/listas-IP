#quantidade de entradas em relação aos elementos para colocar no dicionário
Q = int(input())

banco = dict()

#adicionar elementos em um dicionário
for i in range(Q):
    nome_avaliacao_nota = input().split()
    nome = nome_avaliacao_nota[0]
    avaliacao = nome_avaliacao_nota[1]
    nota = nome_avaliacao_nota[2]
    if nome in banco:
        banco[nome][avaliacao] = nota
    else:
        banco[nome] = dict()
        banco[nome][avaliacao] = nota

#quantidade de entradas para os comandos
N = int(input())

#comandos de adicionar, buscar e consultar
for j in range(N):
    comando = input()
    argumento = input().split()
    if comando == "adicionar":
        nome = argumento[0]
        avaliacao = argumento[1]
        nota = argumento[2]

        if nome in banco:
            banco[nome][avaliacao] = nota
        else:
            banco[nome] = dict()
            banco[nome][avaliacao] = nota

    if comando == "buscar":
        if argumento[0] in banco:
            dicionario_2 = banco[argumento[0]]
            lista = dicionario_2.keys()
            print(f"{argumento[0]}:")
            for key in lista:
                print(f"-{key}: {dicionario_2[key]}")
            print()
        else:
            print(f"{argumento[0]} nao existe no sistema")
            print()

    if comando == "consultar":
        tem = list()
        nao_tem = list()

        for key in banco.keys():
            if argumento[0] in banco[key]:
                tem.append(f"-{key}: {banco[key][argumento[0]]}")
            else:
                nao_tem.append(str(key))
        #comandos para dar as saídas relacionadas com o input desejado
        if len(tem) > 0:
            print(f"{argumento[0]}:")
            for item in tem:
                print(item)
        if len(nao_tem) == 0:
            print("Nao possuem: ")
            print()
        if len(nao_tem) > 0 and len(tem) != 0:
            print(f"Nao possuem: {', '.join(nao_tem)}")
            print()
        if len(tem) == 0:
            print(f"Ninguem possui a avaliacao {argumento[0]}\n")