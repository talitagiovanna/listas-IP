# separar as duas matrizes
N = int(input())
matriz_1 = []
matriz_2 = []
for a in range(N):
    matriz_1.append(input().split())
for b in range(N):
    matriz_2.append(input().split())

u = input().split()


# função de soma de matrizes
def soma(A, B):
    C = []
    nlinhas_A, nlinhas_B = len(A), len(B)
    nCol_A, nCol_B = len(A[0]), len(B[0])

    for i in range(nlinhas_A):
        linha = [0] * nCol_A
        C.append(linha)
        for j in range(nCol_A):
            C[i][j] = int(A[i][j]) + int(B[i][j])
    return C


# função de produto
def produto(A, B):
    C = []
    nlinhas_A, nlinhas_B = len(A), len(B)
    nCol_A, nCol_B = len(A[0]), len(B[0])

    for linha in range(nlinhas_A):
        C.append([])
        for coluna in range(nCol_B):
            C[linha].append(0)
            for k in range(nCol_A):
                C[linha][coluna] += int(A[linha][k]) * int(B[k][coluna])
    return C


for num in u:
    if num == "0":
        matriz_1 = soma(matriz_1, matriz_2)
    if num == "1":
        matriz_2 = soma(matriz_2, matriz_1)
    if num == "2":
        matriz_1 = produto(matriz_1, matriz_2)
    if num == "3":
        matriz_2 = produto(matriz_2, matriz_1)

var =[]
if u[-1] == "0" or u[-1] == "2":
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1)):
            matriz_1[i][j] = str(matriz_1[i][j])
        print(' '.join(matriz_1[i]))
if u[-1] == "1" or u[-1] == "3":
    for i in range(len(matriz_2)):
        for j in range(len(matriz_2)):
            matriz_2[i][j] = str(matriz_2[i][j])
        print(' '.join(matriz_2[i]))