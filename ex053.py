""" 53 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços."""

'''
Primeira possibilidade:

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Neste caso, temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')
'''

# Segunda possibilidade:

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Neste caso, temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')
