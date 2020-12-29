""" 61 - Refaça o desafio 51, lendo o primeiro termo e a razção de uma PA, mostrando os 10 primeiros termos da
progressão, usando a estrutura  WHILE. """

'''
# Exercício 51
p = int(input('Primeiro termo: '))
r = int(input('Razão da progressão: '))
print('Os primeiros dez termos da progressão aritmética serão:', end='')
for p in range(p, p + r * 10, r):
    print(f' {p}', end='')
    print(' →', end='')
print(' FIM')
'''
# Exercício 61
p = int(input('Primeiro termo: '))
r = int(input('Razão da progressão: '))
print('Os primeiros dez termos da progressão aritmética serão:', end='')
c = 1
while c <= 10:
    print(f' {p}', end='')
    print(',' if c < 10 else '', end='')
    p += r
    c += 1
