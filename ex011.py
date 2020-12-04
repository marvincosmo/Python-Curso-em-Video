""" 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m². """

lg = float(input('Qual a largura da parede (em metros)? '))
al = float(input('Qual a altura da parede (em metros)? '))
area = lg * al
tinta = area / 2
print(f'A parede mede {lg:.2f}x{al:.2f}m, tendo, portanto, {area:.2f}m² de área.\nPara pintar esta parede, serão necessários {tinta:.2f} litros de tinta.')