""" 62 - Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
encerrará quando ele disser que quer mostrar mais 0 termos. """

p = int(input('Primeiro termo: '))
r = int(input('Razão da progressão: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f' {p}', end='')
        print(' → ', end='')
        p += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
