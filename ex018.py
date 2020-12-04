""" 18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. """

import math
a = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(a))
c = math.cos(math. radians(a))
t = math.tan(math.radians(a))
print(f'Para o ângulo de {a}°:\nO valor do seno é {s:.2f}\nO valor do cosseno é {c:.2f} e\nO da tangente é {t:.2f}')
