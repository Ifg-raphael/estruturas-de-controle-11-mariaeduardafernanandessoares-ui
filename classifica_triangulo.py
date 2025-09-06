# 3 entradas (a, b e c) e 1 saida (tipo de triangulo).

a = int(input("digite o primeiro valor: "))
b = int(input("digite o segundo valor: "))
c = int(input("digite o terceiro valor: "))


if a == b == c : # fluxo para triangulo equilatero
    print("equilátero")

elif a == b or b == c or c == a : # fluxo para triangulo isoceles
    print("isósceles")

elif a != b and a != c and c != b : 
    print("escaleno")

else:
    print("não forma triangulo")