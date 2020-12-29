""" 60 - Faça um programa que leia um número qualquer e mostre o seu fatorial. """
'''
# Minha resposta -> for
n = int(input('Digite um número para calcular seu Fatorial: '))
print(f'Calculando {n}! = ', end='')
fat = 1
for n in range(n, 0, -1):
    fat *= n
    print(f'{n}', end='')
    print(' x ' if n > 1 else ' = ', end='')
print(f'{fat}')
'''
# Minha resposta -> while
n = int(input('Digite um número para calcular seu Fatorial: '))
print(f'Calculando {n}! = {n} ', end='')
fat = 1
while n != 1:  # ou while n > 0:
    fat *= n
    n -= 1
    print(f'x {n} ', end='')
print(f'= {fat}')
'''
# Versão do professor -> while
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
'''