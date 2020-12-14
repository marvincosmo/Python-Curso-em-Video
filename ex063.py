""" 63 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
sequência de Fibonacci.
Exemplo: 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13"""

# Minha resposta:
print('-' * 59)
print(f"{'Sequência de Fibonacci':^50}")
print('-' * 59)
n = int(input('Quantos termos você quer mostrar? '))
print('~'*40)
print('0 → 1 → ', end='')
a = 0
p = 1
s = 0
c = 1
while c <= n - 2:
    s = p + a
    print(s, end='')
    print(' → ', end='')
    a = p
    p = s
    c += 1
print('FIM')
print('~'*40)
'''
# Resposta do professor
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' →  {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
'''