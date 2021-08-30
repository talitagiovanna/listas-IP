# quantidade de livros
N = int(input())

# livros em ordem alfábetica
livros = []

for i in range(N):
    livros.append(input())
    livros = sorted(livros)

# quantidade de ações
K = int(input())

# comando e nome de livro
comando_livro = []

for j in range(K):
    comando_livro.append(input().split())


# função de busca do livro na lista
def procura(lista, livro, inicio, fim):
    if fim < inicio:
        return -1

    meio = (fim + inicio) // 2

    if lista[meio] > livro:
        return procura(lista, livro, inicio, meio - 1)
    elif lista[meio] < livro:
        return procura(lista, livro, meio + 1, fim)
    else:
        return meio + 1


for n in comando_livro:
    if n[0] == "inserir":
        buscar = procura(livros, n[1], 0, len(livros) - 1)
        if buscar == -1:
            livros.append(n[1])
            livros = sorted(livros)
            achar = procura(livros, n[1], 0, len(livros) - 1)
            print(f"{n[1]} foi colocado na posicao {achar} com sucesso")
        else:
            print(f"{n[1]} ja esta na posicao {buscar}")
    else:
        buscar = procura(livros, n[1], 0, len(livros) - 1)
        if buscar == -1:
            print(f"Nao consegui achar o livro {n[1]}")
        else:
            print(f"O livro {n[1]} esta na posicao {buscar}")