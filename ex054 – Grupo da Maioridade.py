""" 54 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores. """

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for n in range(1, 8, 1):
    ano = int(input(f'em que ano a {n}ª pessoa nasceu? '))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade.\nE também tivemos {menor} pessoas menores de idade.')
