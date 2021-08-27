K = int(input())
J = int(input())

if 1<=K<=1000 and 1<=J<=1000:
    if K%2 ==0 and J%2 ==0:
        print("O Jake conseguiu conjurar sua magia perfeitamente. MAGIC!!\nO Finn nao conseguiu conjurar sua magica perfeitamente. Oh no no no no")
    elif K%2 ==0 and J%2 !=0:
        print("O Jake conseguiu conjurar sua magia perfeitamente. MAGIC!!\nO Finn conseguiu conjurar sua magia perfeitamente. NICE!!")
    elif K%2 !=0 and J%2 ==0:
        print("O Jake nao conseguiu fazer conjurar sua magia perfeitamente. TURURU...\nO Finn nao conseguiu conjurar sua magica perfeitamente. Oh no no no no")
    elif K%2 !=0 and J%2 !=0:
        print("O Jake nao conseguiu fazer conjurar sua magia perfeitamente. TURURU...\nO Finn conseguiu conjurar sua magia perfeitamente. NICE!!")
else:
    print("Entrada invalida")