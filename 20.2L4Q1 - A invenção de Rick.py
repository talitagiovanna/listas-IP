import math

#função principal para calcular as áreas do espaço que irá precisar para guardar o equipamento
def main():
    u = input()
    n = int(input())

    area_q = 0
    area_t = 0
    area_c = 0
    area_r = 0

    for i in range(n):
        medidas = [input().split(": ")]

        for a in medidas:
            if a[0] == "quadrado" and u == "metro":
                quadrado = float(a[1])
                var = area_quadrado(quadrado)
                area_q += var
            elif a[0] == "quadrado" and u == "centimetro":
                quadrado = float(a[1]) / 100
                var_1 = area_quadrado(quadrado)
                area_q += var_1
            if a[0] == "triangulo" and u == "metro":
                lista_var = a[1].split()
                base = float(lista_var[0])
                altura = float(lista_var[1])
                var_2 = area_triangulo(base, altura)
                area_t += var_2
            elif a[0] == "triangulo" and u == "centimetro":
                lista_var_1 = a[1].split()
                base = float(lista_var_1[0]) / 100
                altura = float(lista_var_1[1]) / 100
                var_3 = area_triangulo(base, altura)
                area_t += var_3
            if a[0] == "retangulo" and u == "metro":
                lista_var_2 = a[1].split()
                altura = float(lista_var_2[0])
                base = float(lista_var_2[1])
                var_4 = area_retangulo(altura, base)
                area_r += var_4
            elif a[0] == "retangulo" and u == "centimetro":
                lista_var_3 = a[1].split()
                altura = float(lista_var_3[0])/100
                base = float(lista_var_3[1])/100
                var_5 = area_retangulo(altura, base)
                area_r += var_5
            if a[0] == "circulo" and u == "metro":
                raio = float(a[1])
                var_6 = area_circulo(raio)
                area_c += var_6
            elif a[0] == "circulo" and u == "centimetro":
                raio = float(a[1])/100
                var_7 = area_circulo(raio)
                area_c += var_7
    soma = area_q + area_t + area_r + area_c
    return soma

#funções para calcular a área de cada figura
def area_quadrado(lado):
    area = lado ** 2
    return area


def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


def area_retangulo(altura, base):
    area = altura * base
    return area


def area_circulo(raio):
    area = math.pi * (raio ** 2)
    return area


print(f"Precisarei desocupar {main():.2f} metros quadrados para a maquina")