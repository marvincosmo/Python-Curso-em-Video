""" 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto."""

p = float(input('Qual o preço informado para o produto? R$'))
d = p - p * 5 / 100
print(f'Este produto está com desconto de 5%!\nEm vez de pagar R${p:.2f}, você vai pagar R${d:.2f}!')
