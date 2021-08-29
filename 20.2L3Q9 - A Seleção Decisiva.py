#número de alunos a serem analisados
X = int(input())

#lista com nomes dos magos e seus respectivos poderes
nome_poder = []

mais_fortes = []
mais_fracos = []

#inserir nomes e poderes em uma lista
for i in range(X):
    nome_poder.append(input().split())

maior = menor = int(nome_poder[0][1])

for poder in nome_poder:
    if int(poder[1]) > maior:
        maior = int(poder[1])
        mais_fortes = []
        mais_fortes.append(poder[0])
    elif int(poder[1]) == maior:
        mais_fortes.append(poder[0])
    if int(poder[1]) < menor:
        menor = int(poder[1])
        mais_fracos = []
        mais_fracos.append(poder[0])
    elif int(poder[1]) == menor:
        mais_fracos.append(poder[0])


print(f"Sr Dumbledore, o maior poder de magia foi {maior}, e a nova força será composta pelo(s) seguinte(s) aluno(s): {', '.join(mais_fortes)}. Infelizmente, o menor nível de poder foi {menor} e os aluno(s) expulso(s): {', '.join(mais_fracos)}.")