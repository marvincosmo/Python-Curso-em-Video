""" 55 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

maior = 0
menor = 0
for p in range(1, 6, 1):
    peso = float(input(f'Qual é o peso da {p}ª pessoa (em quilos)? '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi de {maior}Kg.\nO menor peso lido foi de {menor}Kg.')
