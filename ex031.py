""" 31 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas. """

d = float(input('Qual é a distância do trajeto da viagem, em Km? '))
print(f'Você está prestes a começar uma viagem de \33[92m{d}Km\33[m, ', end='')
if d <= 200:
    p = d * 0.5
    print(f'e o preço da passagem será \33[32;7mR${p:.2f}\33[m.')
else:
    p = d * 0.45
    print(f'e o preço da passagem será \33[32;7mR${p:.2f}\33[m.')
    