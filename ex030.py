""" 30 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""

n = int(input('\33[94mMe diga um número qualquer:\33[m '))
if n % 2 == 0:
    print(f'O número {n} é \33[96mPAR\33[m.')
else:
    print(f'O número {n} é \33[95mÍMPAR\33[m.')
