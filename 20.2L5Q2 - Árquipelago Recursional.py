ilha_atual = int(input())
ilha_desejada = int(input())
suprimento = int(input())

def recursional(ilha_inicial, ilha_tesouro, contador):

    if contador == suprimento and ilha_inicial == ilha_tesouro:
        #print("Já estamos aqui, marujo!")
        return "Já estamos aqui, marujo!"

    elif ilha_inicial == ilha_tesouro:
        if contador == 0:
            #print("Chegamos pela pele dos dentes de Netuno!")
            return "Chegamos pela pele dos dentes de Netuno!"

        else:
            #print("O tesouro é nosso")
            return "O tesouro é nosso"

    else:
        if contador > 0:
            return recursional(ilha_inicial * 5, ilha_tesouro, contador - 1) or \
                   recursional(ilha_inicial // 2, ilha_tesouro, contador - 1) or \
                   recursional(ilha_inicial + 1, ilha_tesouro, contador - 1)
        else:
            # print("Vamos precisar de um barco maior")
            return ""



resposta = recursional(ilha_atual, ilha_desejada, suprimento)
if(not resposta):
    print("Vamos precisar de um barco maior")
else:
    print(resposta)