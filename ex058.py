""" 58 - Melhore o jogo do desafio 028, onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o
jogador vai tentar adivinhar até acertar, mostrando, no final, quantos palpites foram necessários para vencer. """

'''
# Minha versão
from random import randint
print('\033[33m-=-\033[m' * 21)
print('\033[34mPensei em um número entre 0 e 10. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m' * 21)
computador = randint(0, 10)  # A jogada do computador
tentativas = 0
jogador = -1
while jogador != computador:
    jogador = int(input('Em qual número eu pensei? '))  # A jogada do jogador
    if jogador < computador:
        print('\033[91mMais... Tente outra vez!\033[m')
    elif jogador > computador:
        print('\033[31mMenos... Tente outra vez!\033[m')
    tentativas += 1
if jogador == computador:
    print(f'\033[32mPARABÉNS! Você adivinhou em {tentativas} tentativas.\033[m')
'''
# Versão do professor
from random import randint
print('\033[33m-=-\033[m' * 21)
print('\033[34mPensei em um número entre 0 e 10. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m' * 21)
computador = randint(0, 10)  # A jogada do computador
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Em qual número eu pensei? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[91mMais... Tente outra vez!\033[m')
        elif jogador > computador:
            print('\033[31mMenos... Tente outra vez!\033[m')
print(f'\033[32mPARABÉNS! Você adivinhou em {palpites} tentativas.\033[m')
