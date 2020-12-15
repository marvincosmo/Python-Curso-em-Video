""" 15 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. """

d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros ele rodou? '))
pg = d * 60 + km * 0.15
print(f'Tendo sido alugado por {d} dias e tendo rodado {km} quilômetros, o valor total a pagar é de R${pg:.2f}.')
