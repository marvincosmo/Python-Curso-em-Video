""" 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. """

import math
op = float(input('Qual a medida do cateto oposto? '))
ad = float(input('Qual a medida do cateto adjacente? '))
hp = math.hypot(op, ad)  # hp = math.sqrt(pow(op, 2) + pow(ad, 2)) OU hp = (op ** 2 + ad ** 2) ** (1 / 2)
print(f'Tendo o cateto oposto a medida de {op} e o cateto adjacente {ad}, a hipotenusa será {hp:.2f}.')
