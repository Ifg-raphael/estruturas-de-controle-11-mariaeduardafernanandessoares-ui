# 3 entradas  e 1 saida (tipo de triangulo).

lados = input("digite os lados do triangulos: ")

lados_em_texto = lados.split()

lados_do_triangulo = []

for i in lados_em_texto:
    lado_convertido = float(i)
    lados_do_triangulo.append(lado_convertido)


if lados_do_triangulo[0] == lados_do_triangulo[1] == lados_do_triangulo[2]:
    print("equilátero")
    
elif lados_do_triangulo[0] == lados_do_triangulo[1] or lados_do_triangulo[2] == lados_do_triangulo[1] or lados_do_triangulo[2] == lados_do_triangulo[0]:
    print("isósceles")

elif lados_do_triangulo[0] != lados_do_triangulo[1] and lados_do_triangulo[0] != lados_do_triangulo[2] and lados_do_triangulo[1] != lados_do_triangulo[2]:
    print("escaleno")

else:
    print("Não forma triângulo")