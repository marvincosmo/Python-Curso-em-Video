""" 068 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """

from random import randint
print('=-='*11)
print('VAMOS JOGAR PAR OU ÍMPAR'.center(33))
print('=-='*11)
v = 0
while True:
    c = randint(0, 10)
    j = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    s = c + j
    print('-'*33)
    print(f'''Você jogou {j} e o computador, {c}.
Total = {s} → ''', end='')
    if s % 2 == 0:
        r = 'P'
        print('PAR')
    else:
        r = 'I'
        print('ÍMPAR')
    print('-'*33)
    if pi == r:
        print('''Você VENCEU!
Vamos jogar novamente...''')
        print('=-=' * 11)
        v += 1
    else:
        print('Você PERDEU.')
        print('=-=' * 11)
        break
print(f'GAME OVER!', end=' ')
if v == 0:
    print('Você não venceu nenhuma!')
elif v == 1:
    print('Você só venceu uma vez...')
else:
    print(f'Você venceu {v} vezes.')
