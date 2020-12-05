""" 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:
 - Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER """

from datetime import date
atual = date.today().year
ano = int(input('Ano de Nascimento: '))
idade = atual - ano
print(f'''O atleta tem {idade} anos.
Classificação:''', end=' ')
if idade <=9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')

# Esta outra resposta foi criada pelo Marcos do futuro:
"""
from datetime import date
atual = date.today().year
while True:
    ano = int(input('Ano de Nascimento (Digite 0 para parar): '))
    if ano == 0:
        break
    idade = atual - ano
    print(f'''    O atleta tem {idade} anos.
    Classificação:''', end=' ')
    if idade <= 9:
        print('MIRIM')
    elif idade <= 14:
        print('INFANTIL')
    elif idade <= 19:
        print('JÚNIOR')
    elif idade <= 25:
        print('SÊNIOR')
    else:
        print('MASTER')
print('Fim do programa')
"""