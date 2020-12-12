""" 45 - Crie um programa que faça o computador jogar Jokenpô com você. """
"""
from random import randint
from time import sleep
tipos = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
computador = randint(0, 2)
jogador = int(input('Qual é a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Opção inválida.')
else:
    print('JO', end='')
    sleep(1)
    print('KEN', end='')
    sleep(1)
    print('PO!')
    sleep(0.3)
    print('=-' * 16)
    print(f'O computador jogou {tipos[computador]}')
    print(f'O jogador jogou {tipos[jogador]}')
    print('=-' * 16)
    if computador == jogador:
        print('EMPATE')
    elif computador == 0:  # PEDRA
        if jogador == 1:
            print('O JOGADOR VENCE!')
        elif jogador == 2:
            print('O COMPUTADOR VENCE.')
    elif computador == 1:  # PAPEL
        if jogador == 2:
            print('O JOGADOR VENCE!')
        elif jogador == 0:
            print('O COMPUTADOR VENCE.')
    elif computador == 2:  # TESOURA
        if jogador == 0:
            print('O JOGADOR VENCE!')
        elif jogador == 1:
            print('O COMPUTADOR VENCE.')

# Esta também é uma alternativa:
'''if jogador == 0 or jogador == 1 or jogador == 2:
    print('JO', end='')
    sleep(1)
    print('KEN', end='')
    sleep(1)
    print('PO!')
    sleep(0.3)
    print('=-' * 16)
    print(f'O computador jogou {tipos[computador]}')
    print(f'O jogador jogou {tipos[jogador]}')
    print('=-' * 16)
    if computador == jogador:
        print('EMPATE')
    elif computador == 0:  # PEDRA
        if jogador == 1:
            print('O JOGADOR VENCE!')
        elif jogador == 2:
            print('O COMPUTADOR VENCE.')
    elif computador == 1:  # PAPEL
        if jogador == 2:
            print('O JOGADOR VENCE!')
        elif jogador == 0:
            print('O COMPUTADOR VENCE.')
    elif computador == 2:  # TESOURA
        if jogador == 0:
            print('O JOGADOR VENCE!')
        elif jogador == 1:
            print('O COMPUTADOR VENCE.')
else:
    print('Opção inválida.')'''
"""
# Resposta do professor:
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0:  # PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:  # PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:  # TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
    