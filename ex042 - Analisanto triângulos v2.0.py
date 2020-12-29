""" 42: Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes """

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print('Os segmentos acima', end=' ')
if a < b + c and b < a + c and c < a + b:
    print('\033[32mPODEM FORMAR\033[m um triângulo', end=' ')
    if a == b == c:
        print('\033[34mEQUILÁTERO\033[m.')
    elif a != b != c != a:
        print('\033[31mESCALENO\033[m.')
    else:
        print('\033[33mISÓSCELES\033[m.')
else:
    print('\033[35mNÃO PODEM\033[m formar um triângulo.')
