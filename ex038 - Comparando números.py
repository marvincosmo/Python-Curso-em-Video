""" 38 - Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais """

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
if a > b:
    print('O PRIMEIRO valor é o maior.')
elif a < b:
    print('O SEGUNDO valor é o maior.')
else:  # caso queira, aqui também pode ser: elif a == b:
    print('Não existe valor maior, ambos são iguais.')
