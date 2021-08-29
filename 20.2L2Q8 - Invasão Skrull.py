meta_de_infiltrados = int(input())
quantidade_skrulls = int(input())
numero_acontecimentos = int(input())
nivel_de_alerta = 0

for i in range(numero_acontecimentos):
    acontecimento = input()

    if acontecimento == "Substituicao":
        novos_infiltrados = int(input())
        quantidade_skrulls += novos_infiltrados
    elif acontecimento == "Contra-ataque":
        detectados = int(input())
        quantidade_skrulls -= detectados
    else:
        nivel_de_alerta += 30

    if quantidade_skrulls == 0:
        break
    elif nivel_de_alerta >= 100:
        break
    elif quantidade_skrulls >= meta_de_infiltrados:
        break

if quantidade_skrulls >= meta_de_infiltrados:
    print("Ordenar ataque imediatamente, dessa vez dominaremos a Terra")
elif nivel_de_alerta >= 100:
    print("Não vale a pena continuar, vamos recuar e bolar um novo plano")
elif 0 < quantidade_skrulls < meta_de_infiltrados:
    print("Ainda não estamos preparados para atacar, vamos esperar mais um pouco")

if quantidade_skrulls == 0:
    print("Falhamos completamente, não há mais nenhum Skrull infiltrado")