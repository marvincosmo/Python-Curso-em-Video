""" 25 - Crie um programa que leia o nome de uma pessoa e diga se ele tem 'SILVA'. """

nome = str(input('Qual é o seu nome completo? ')).strip().upper()
print('Seu nome tem Silva?', end=' ')
print('SILVA' in nome)

'''
# Esta outra resposta foi criada pelo Marcos do futuro:

nome = str(input('Qual é o seu nome completo? ')).strip().upper()
print('Seu nome tem Silva?', end=' ')
r = 'SILVA' in nome
if r:  # É o mesmo que escrever if r == True:
    print('SIM')
else:
    print('NÃO')
'''
'''
# Esta também:

nome = str(input('Qual é o seu nome completo? ')).strip().upper()
print('Seu nome tem Silva?', end=' ')
r = 'SILVA' in nome
print('SIM' if r else 'NÃO')
'''
