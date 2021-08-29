N = int(input())

for i in range(N):
    mensagem = input()
    tamanho = int(len(mensagem)/2)
    mensagem_decodificada = ""
    for c in range(tamanho):
        x = mensagem[c]
        y = mensagem[(len(mensagem) - 1) - c]

        mensagem_decodificada += (chr(int(x + y)))
    print(mensagem_decodificada)