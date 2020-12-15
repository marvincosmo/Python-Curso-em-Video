""" 03 - Crie um script Python que leia dois números e tente mostrar a soma entre eles."""

print('=' * 6, ' DESAFIO 03 - SOMANDO DOIS NÚMEROS ', '=' * 6)
print('\n*** MODO QUE VAI DAR RUIM ***')
n1 = input('Digite um número: ')
n2 = input('Digite mais um número: ')
s = n1 + n2
print(f'A soma entre {n1} e {n2} é {s}.')
print('\n*** MODO QUE VAI DAR BOM ***')
n3 = int(input('Digite um número: '))
n4 = int(input('Digite mais um número: '))
s = n3 + n4
print(f'A soma entre {n3} e {n4} é {s}.')
