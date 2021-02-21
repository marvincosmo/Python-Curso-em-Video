""" 87 - Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""
# Minha resposta:
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terceira = maior = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            terceira += matriz[l][2]
        if matriz[1][c] == 1:
            maior = matriz[1][c]
        else:
            if matriz[1][c] > maior:
                maior = matriz[1][c]
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares digitados é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceira}.')
print(f'O maior valor da segunda linha é {maior}.')
"""
# Resposta do professor:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terceira = maior = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares digitados é {pares}.')
for l in range(0, 3):
    terceira += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {terceira}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}.')
