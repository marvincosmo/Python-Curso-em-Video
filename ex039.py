""" 39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda
vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu
programa também deverá mostrar o tempo que falta ou que passou do prazo. """

from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
alistamento = ano + 18
if idade < 18:
    diferença = 18 - idade
    if diferença > 1:
        print(f'Ainda faltam {diferença} anos para o seu alistamento.')
    else:
        print(f'Ainda falta {diferença} ano para o seu alistamento.')
    print(f'Seu alistamento será em {alistamento}.')
elif idade > 18:
    diferença = idade - 18
    if diferença > 1:
        print(f'Você já deveria ter se alistado há {diferença} anos.')
    else:
        print(f'Você já deveria ter se alistado há {diferença} ano.')
    print(f'Seu alistamento foi em {alistamento}.')
else:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
