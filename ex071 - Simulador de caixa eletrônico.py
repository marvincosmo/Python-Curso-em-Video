""" 71 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. """

print('='*30)
print('Banco BancaRio'.center(30))
print('='*30)
v = int(input('Que valor você quer sacar? R$'))
c = 50
t = 0
while True:
    if v >= c:
        v -= c
        t += 1
    else:
        if t > 0:
            print(f'Total de {t} cédulas de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        t = 0
        if v == 0:
            break
print('='*30)
print('Muito obrigado por escolher o Banco BancaRio! Aguardamos seu retorno.')
