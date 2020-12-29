""" 50 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o
valor digitado for ímpar, desconsidere-o. """

cont = 0
soma = 0
for n in range(1, 7):
    num = int(input(f'Informe o {n}º valor: '))
    if n % 2 == 0:
        cont += 1
        soma += num
print(f'A soma dos {cont} números pares informados é igual a {soma}.')
