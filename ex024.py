""" 24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome 'SANTO'. """

cidade = str(input('Em que cidade você nasceu? ')).strip().upper()
print('SANTO' in cidade[:5])

''' 
# Esta outra resposta foi criada pelo Marcos do futuro:

cidade = str(input('Em que cidade você nasceu? ')).strip().upper()
print('Existe a palavra "Santo" no início do nome desta cidade?', end=' ')
r = 'SANTO' in cidade[:5]
if r:  # É o mesmo que escrever if r == True:
    print('SIM')
else:
    print('NÃO')
'''
'''
# Esta também:

cidade = str(input('Em que cidade você nasceu? ')).strip().upper()
print('Existe a palavra "Santo" no início do nome desta cidade?', end=' ')
r = 'SANTO' in cidade[:5]
print('SIM' if r else 'NÃO')
'''
