""" 48 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
encontram no intervalo de 1 até 500. """

cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        cont += 1  # cont = cont + 1
        soma += c  # soma = soma + c
print(f'\n\nA soma de todos os {cont} valores solicitados é igual a {soma}.')
