n = int(input())
soma_1 = 0
soma_2 = 0
fatorial = 1
a = 2

for i in range(n):
    v = int(input())
    if i%2 != 0:
        soma_1 += v
    else:
        soma_2 += v

while a <= n:
    fatorial = fatorial*a
    a +=1

if n%2 == 0:
    codigo = fatorial - (soma_2)*(soma_1)
else:
    codigo = fatorial - (soma_2)*(soma_1)
print(codigo)