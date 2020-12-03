# Sequência de números de 1 a 10.
'''
cont = 1
while cont <= 10:
    print(cont, '→ ', end='')
    cont += 1
print('Acabou')
'''
# Loop infinito com o mesmo algoritmo, apenas trocando o limite de 10 números para "enquanto for verdade".
'''
cont = 1
while True:
    print(cont, '→ ', end='')
    cont += 1
print('Acabou')
'''
# Tratando vários valores COM GAMBIARRA:
'''
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999  # GAMBIARRA!
print(f'A soma vale {s}.')
'''
# Tratando vários valores SEM GAMBIARRA:
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')
