""" 57 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto. """

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
if sexo in 'Mm':
    print('Sexo MASCULINO registrado com sucesso.')
elif sexo in 'Ff':
    print('Sexo FEMININO registrado com sucesso')
