Atk_F = int(input())
Def_F = int(input())
Pdv_F = int(input())
Atk_J = int(input())
Def_J = int(input())
Pdv_J = int(input())
Atk_S = int(input())
Def_S = int(input())
Pdv_S = int(input())
B = int(input())

Def_maior = Def_F

if Def_J > Def_maior:
    Def_maior = Def_J

if (2*Def_maior) < Atk_S:
    Dn_S = int(Atk_S*1.5)
elif (2*Def_maior) >= Atk_S > Def_maior:
    Dn_S = int(Atk_S)
else:
    Dn_S = int(Atk_S*0.5)

if (2*Def_S) < Atk_F:
    Dn_F = int(Atk_F*1.5)
elif (2*Def_S) >= Atk_F > Def_S:
    Dn_F = int(Atk_F)
else:
    Dn_F = int(Atk_F*0.5)

if (2*Def_S) < Atk_J:
    Dn_J = int(Atk_J*1.5)
elif (2*Def_S) >= Atk_J > Def_S:
    Dn_J = int(Atk_J)
else:
    Dn_J = int(Atk_J*0.5)

if Dn_S == 0:
    Dn_S = 1

if Dn_F == 0:
    Dn_F = 1

if Dn_J == 0:
    Dn_J = 1

morte_S = Pdv_S/ (Dn_F + Dn_J)
morte_F = Pdv_F/ Dn_S
morte_J = Pdv_J/ Dn_S

if morte_J > morte_S and morte_F > morte_S:
    Pdv_Ja = Pdv_J - (morte_S*Dn_S)
    Pdv_Finn = Pdv_F - (morte_S*Dn_S)
    Pdv_T = Pdv_Ja + Pdv_Finn
    if Pdv_T > B:
        print("Derrotamos a serpente\ne o tesouro e nosso!")
    else:
        print("Derrotamos a serpente\nmas nao temos forcas para abrir o bau")
elif morte_F < morte_S or morte_J < morte_S:
    if Pdv_J < Pdv_F:
        print("Jake, nao!")
    elif Pdv_F < Pdv_J:
        print("Finn, nao!")
    else:
        print("Amigo, nao!")
else:
    print("Nao conseguimos fazer mais nada")