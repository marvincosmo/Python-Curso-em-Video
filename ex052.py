""" 52 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

n = int(input('Informe um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\33[34m', end=' ')
        cont += 1
    else:
        print('\33[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\33[mO número {n} foi divisível {cont} vezes.')
if cont == 2:
    print('E por isso ele É PRIMO.')
else:
    print('E por isso ele NÃO É PRIMO.')
