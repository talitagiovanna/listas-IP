N = int(input())

operadores = []


def tratar_numeros(string):
    string = string.split(',')
    return (int(string[0][1:])), (int(string[1][:-1]))


def soma(valor1, valor2):
    valor1 = tratar_numeros(valor1)
    valor2 = tratar_numeros(valor2)

    a = valor1[0]
    b = valor1[1]
    c = valor2[0]
    d = valor2[1]

    valor_1 = a + c
    valor_2 = b + d
    print(f"({valor_1},{valor_2})")


def subtracao(valor1, valor2):
    valor1 = tratar_numeros(valor1)
    valor2 = tratar_numeros(valor2)

    a = valor1[0]
    b = valor1[1]
    c = valor2[0]
    d = valor2[1]

    valor_1 = a - c
    valor_2 = b - d
    print(f"({valor_1},{valor_2})")


def produto(valor1, valor2):
    valor1 = tratar_numeros(valor1)

    a = valor1[0]
    b = valor1[1]
    valor_1 = a * int(valor2)
    valor_2 = b * int(valor2)

    print(f"({valor_1},{valor_2})")


def escalar(valor1, valor2):
    valor1 = tratar_numeros(valor1)
    valor2 = tratar_numeros(valor2)

    a = valor1[0]
    b = valor1[1]
    c = valor2[0]
    d = valor2[1]

    primeiro = a * c
    segundo = b * d

    valor = primeiro + segundo
    return print(f"{valor}")


dicionario = {'+': soma, '-': subtracao, '*': produto, '.': escalar}

for i in range(N):
    valor_operador = input().split()
    operadores = valor_operador[1]
    n1 = valor_operador[0]
    n2 = valor_operador[2]

    resultado = dicionario[operadores](n1, n2)