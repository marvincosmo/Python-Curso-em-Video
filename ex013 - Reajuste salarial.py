""" 13 - Faça um algoritmo que lei o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""

s = float(input('Qual é o salário do funcionário? R$'))
a = s * 15 / 100
f = s + a
print(f'Este funcionário teve seu salário reajustado em 15%.\nCom o aumento de R${a:.2f}, em vez de R${s:.2f}, ele vai receber R${f:.2f}')
