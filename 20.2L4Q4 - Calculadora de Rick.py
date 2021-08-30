K = int(input())

lista = []
for i in range(K):
    lista.append(input().split())


def calculadora(lista):
    RESP = 0
    lista_resposta = []
    for j in lista:
        if j[1] == "@":
            if j[0] == "RESP":
                A = RESP
                B = int(j[2])
                RESP = (A ** B) - A
                lista_resposta.append(RESP)
            else:
                A = int(j[0])
                B = int(j[2])

                RESP = (A ** B) - A
                lista_resposta.append(RESP)
        elif j[1] == "?":
            if j[0] == "RESP":
                A = RESP
                B = int(j[2])
                RESP = ((A ** B) - A) * B
                lista_resposta.append(RESP)
            else:
                A = int(j[0])
                B = int(j[2])

                RESP = ((A ** B) - A) * B
                lista_resposta.append(RESP)
        elif j[1] == ">":
            if j[0] == "RESP":
                A = RESP
                B = int(j[2])
                fatorial = 1
                n = 2
                while n <= A:
                    fatorial = fatorial * n
                n += 1

                RESP = ((fatorial ** B) - fatorial) * B
                lista_resposta.append(RESP)
            else:
                A = int(j[0])
                B = int(j[2])
                fatorial = 1
                n = 2
                while n <= A:
                    fatorial = fatorial * n
                    n += 1

                RESP = ((fatorial ** B) - fatorial) * B
                lista_resposta.append(RESP)
        elif j[1] == "<":
            if j[0] == "RESP":
                A = RESP
                B = int(j[2])
                fatorial = 1
                n = 2
                while n <= B:
                    fatorial = fatorial * n
                    n += 1

                RESP = ((fatorial ** A) - fatorial) * A
                lista_resposta.append(RESP)
            else:
                fatorial = 1
                n = 2
                A = int(j[0])
                B = int(j[2])
                while n <= B:
                    fatorial = fatorial * n
                    n += 1

                RESP = ((fatorial ** A) - fatorial) * A
                lista_resposta.append(RESP)
    return lista_resposta


A = calculadora(lista)

for j in A:
    print(j)