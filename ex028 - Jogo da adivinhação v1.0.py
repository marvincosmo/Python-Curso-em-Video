""" 28 - Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
ou perdeu. """

from random import randint
from time import sleep
print('\33[33m-=-' * 23, '\33[m')
print('\33[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\33[m')
print('\33[33m-=-' * 23, '\33[m')
computador = randint(0, 5)  # Número escolhido pelo computador.
sleep(2)
jogador = int(input('Em que número eu pensei? '))  # Palpite do jogador.
print('\33[35mPROCESSANDO.\33[m', end='')
sleep(1)
print('\33[35m.\33[m', end='')
sleep(1)
print('\33[35m.\33[m')
sleep(1)
if computador == jogador:
    print(f'\33[32mPARABÉNS! Você adivinhou!\33[m')
else:
    print(f'\33[31mGANHEI! Eu pensei no número {computador} e não no {jogador}!\33[m')
