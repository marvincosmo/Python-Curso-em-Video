""" 65 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores. """

n = s = c = m = maior = menor = 0
r = ''
while r in 'sS':
    n = int(input('Digite um número: '))
    c += 1
    s += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continar [S/N]? ')).strip().upper()[0]
m = s / c
print(f'''Você digitou {c} números e a média deles foi {m}.
O maior valor foi {maior} e o menor foi {menor}.''')
