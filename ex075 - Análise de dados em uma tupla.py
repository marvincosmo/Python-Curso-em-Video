""" 75 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. """

n = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {n}')
nove = n.count(9)
if nove == 0:
    print('O valor 9 não apareceu nenhuma vez.')
elif nove == 1:
    print(f'O valor 9 só apareceu {nove} vez.')
else:
    print(f'O valor 9 apareceu {nove} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for p in n:
    if p % 2 == 0:
        print(p, end=' ')
