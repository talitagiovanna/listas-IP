R1, R2, R3, R4 = int(input()), int(input()), int(input()), int(input())
F1, F2, F3, F4 = int(input()), int(input()), int(input()), int(input())
Vidafinn = 100
Vidarei = 100
Dano1 = R1 + R2 + R3 + R4
Dano2 = F1 + F2 + F3 + F4
if R1 >=0:
    Vidafinn = Vidafinn - R1
    if R2 >= 0:
        Vidafinn = Vidafinn - R2
        if R3 >= 0:
            Vidafinn = Vidafinn - R3
            if R4 >= 0:
                Vidafinn = Vidafinn - R4
if F1 >= 0:
    Vidarei = Vidarei - F1
    if F2 >=0:
        Vidarei = Vidarei - F2
        if F3 >= 0:
            Vidarei = Vidarei - F3
            if F4 >= 0:
                Vidarei = Vidarei - F4
if Vidarei < Vidafinn:
    print(f"Apos esquivar de todas as magias do mago, Finn venceu a luta e deu {Dano2} de dano, deixando o Rei Gelado com {Vidarei} de vida restante.")
elif Vidarei > Vidafinn:
    print(f"As magias foram implacaveis, Finn lutou com todas suas forcas, mas o Rei Gelado foi vitorioso. O mago conseguiu dar {Dano1} de dano, deixando Finn com {Vidafinn} de vida restante.")
else:
    print(f"Apesar dos esforcos, ninguem foi capaz de ser vitorioso, ficando com exatamente {Vidafinn} de vida restante cada, portanto terao que resolver suas intrigas em outra oportunidade.")