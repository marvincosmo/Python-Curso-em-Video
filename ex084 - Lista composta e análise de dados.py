""" 84 -  Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

individuo = []
grupo = list()
maior = menor = 0
while True:
    individuo.append(str(input('Nome: ')))
    individuo.append(float(input('Peso (Kg): ')))
    if len(grupo) == 0:
        maior = menor = individuo[1]
    else:
        if individuo[1] > maior:
            maior = individuo[1]
        if individuo[1] < menor:
            menor = individuo[1]
    grupo.append(individuo[:])
    individuo.clear()
    r = ' '
    while r not in 'NnSs':
        r = str(input('Quer continuar (S/N)')).strip()[0]
    if r in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(grupo)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
