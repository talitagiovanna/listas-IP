X = input()
X = ord(X)
Y = int(input())
Fx = input()
Fx = ord(Fx)
Fy = int(input())

if Fx != X or Fy != Y:
    Ah = int(input())
    Av = int(input())
    Fy = (Fy + Av)%5
    Fx = (Fx + Ah)%5 + 65
    if Fx != X or Fy != Y:
        Ah = int(input())
        Av = int(input())
        Fy = (Fy + Av)%5
        Fx = (Fx + Ah)%5 + 65
        if Fx != X or Fy != Y:
            print("Bem... ainda nao estamos mortos ne?")
        else:
            print("Finn e Jake conseguiram sair do labirinto!")
    else:
        print("Finn e Jake conseguiram sair do labirinto!")
else:
    print("Finn e Jake conseguiram sair do labirinto!")
