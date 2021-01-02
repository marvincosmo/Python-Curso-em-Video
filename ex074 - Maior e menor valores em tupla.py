""" 74 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. """
# Minha resposta:
"""
from random import randint
maior = menor = 0
tupla = tuple(randint(1, 10) for n in range(0, 5))
print(f'Os valores sorteados foram: {tupla[0]} {tupla[1]} {tupla[2]} {tupla[3]} {tupla[4]}')
for n in range(0, 5):
    if n == 0:
        maior = tupla[n]
        menor = tupla[n]
    else:
        if tupla[n] > maior:
            maior = tupla[n]
        if tupla[n] < menor:
            menor = tupla[n]
print(f'''O maior valor sorteado foi {maior}.
O menor valor sorteado foi {menor}.''')
"""
# Resposta do professor:
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')  # Também pode ser: print(n, end=' ')
print(f'''\nO maior valor sorteado foi {max(numeros)}.
O menor valor sorteado foi {min(numeros)}.''')
