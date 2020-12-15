""" 23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. """

from time import sleep
n = int(input('Informe um número: '))
print(f'Analisando o número {n}...')
sleep(2)
u = n // 1 % 10  # u = n % 10 (esta forma é mais econômica, mas a outra é mais didática)
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')
