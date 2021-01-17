""" 81 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista. """

# Minha resposta:
"""
c = 0
lista = []  # ou list()
while True:
    lista.append(int(input('Informe um número para ser incluído na lista: ')))
    c += 1
    r = str(input('Gostaria de continuar [S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Foram digitados {c} números.')
lista.sort(reverse=True)
print(f'A lista de valores, ordenada de forma decrescente: {lista}')
if 5 in lista:
    print(f'O número 5 foi digitado nesta lista, na posição {lista.index(5)}.')
else:
    print('O número 5 não foi digitado nesta lista.')
"""
# Resposta do professor:
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
