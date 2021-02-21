""" 85 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. """

# Minha resposta:
"""
numeros = list()
pares = []
impares = []
for v in range(1, 8):
	numeros.append(int(input(f'Digite o {v}º valor: ')))
for n in numeros:
	if n % 2 == 0:
		pares.append(n)
	else:
		impares.append(n)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(pares)}')
print(f'Os valores ímpares digitados foram: {sorted(impares)}')
"""

# Resposta do professor:
numeros = [[], []]
valor = 0
for c in range(1, 8):
	valor = int(input(f'Digite o {c}º valor: '))
	if valor % 2 == 0:
		numeros[0].append(valor)
	else:
		numeros[1].append(valor)
print('-=' * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
