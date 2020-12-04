""" 27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente. """

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Muito prazer em te conhecer!')
dividido = nome.split()
print(f'Seu primeiro nome é {dividido[0]}')
print(f'Seu último nome é {dividido[len(dividido) - 1]}')
