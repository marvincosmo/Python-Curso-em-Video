""" 88 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. """
# Minha resposta:
"""
from time import sleep
from random import randint
jogo = []
palpite = list()
print('-' * 30)
print(f"{'JOGA NA MEGA SENA':^30}")
print('-' * 30)
q = int(input('Quantos jogos você quer que eu sorteie? '))
print('-' * 30)
print(f"{'SORTEANDOS OS NÚMEROS...':^30}")
sleep(1)
for r in range(0, q):
    print(f'{r+1}º Jogo:', end='')
    for n in range(0, 6):
        m = randint(1, 60)
        if m not in jogo:
            jogo.append(m)
    print(sorted(jogo))
    jogo.clear()
    sleep(1)
"""
# Resposta do professor:
from random import randint
from time import sleep
lista = list()
jogos = []
print('-' * 30)
print(f"{'JOGA NA MEGA SENA':^30}")
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
