""" 82 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
das três listas geradas. """

# Minha resposta:
"""
lista = []  # ou list()
pares = []
impares = []
while True:
    n = (int(input('Digite um número: ')))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Gostaria de continuar [S/N]? '))[0]
    if r in 'Nn':
        break
print('=-'*30)
print(f'Lista com todos os números: {lista}')
print(f'Lista dos números pares: {pares}')
print(f'Lista dos números ímpares: {impares}')
"""
# Resposta do professor:
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('=-'*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
