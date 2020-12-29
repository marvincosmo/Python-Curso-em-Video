
""" 32 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano \33[34m{ano}\33[m é \33[32mBISSEXTO\33[m.')
else:
    print(f'O ano \33[34m{ano}\33[m \33[31mNÃO\33[m é \33[31mBISSEXTO\33[m.')
