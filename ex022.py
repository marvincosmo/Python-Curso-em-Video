""" 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo, (sem considerar espaços).
- Quantas letras tem o primeiro nome."""

from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
sleep(2)
print(f'Seu nome, em maíusculas, é {nome.upper()}')
print(f'Seu nome, em minúsculas, é {nome.lower()}')
print(f"Seu nome tem, ao todo, {len(nome) - nome.count(' ')} letras")
# print(f"Seu primeiro nome tem {nome.find(' ')} letras")
dividido = nome.split()
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras')
