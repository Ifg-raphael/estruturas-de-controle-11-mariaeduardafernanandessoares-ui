#input de dados na mesma linha
lados = input("digite os lados do triangulos: ")
#pegando as strings de entrada e convertendo para string separada
lados_em_texto = lados.split()

lados_do_triangulo = [] #lista pra armaxzenar os valores entrados

for i in lados_em_texto: # for para coneverter cada um dos valores
    lado_convertido = float(i)# conversao para float
    lados_do_triangulo.append(lado_convertido)#adicionando valor convertido a lista

a = lados_do_triangulo[0] #atribuçao de variavel a
b = lados_do_triangulo[1] #atribuçao de variavel b
c = lados_do_triangulo[2] #atribuçao de variavel c

#verifica se as somas dos lados são maiores que o terceiro lado, se é mesmo um triangulo.
if (a + b > c) and (a + c > b) and (b + c > a):
    #verificar qual o tipo de triângulo
    if a == b == c:
        print("equilátero")
    elif a != b and a != c and b != c:
        print("escaleno")
    else: # Se não for equilátero nem escaleno, só pode ser isósceles
        print("isósceles")
else:
    # Se a primeira condição for falsa, não é um triângulo
    print("Não forma triângulo")