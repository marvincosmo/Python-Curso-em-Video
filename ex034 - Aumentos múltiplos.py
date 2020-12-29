""" 34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. """

salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    aumento = salario + salario * 10 / 100
else:
    aumento = salario + salario * 15 / 100
print(f'Com o reajuste proposto, o salário do funcionário passa de \33[31mR${salario:.2f}\33[m para \33[96mR${aumento:.2f}\33[m.')
