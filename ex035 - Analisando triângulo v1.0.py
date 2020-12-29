""" 35 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
triângulo. """

print('\33[33m-=\33[m' * 14)
print('\33[35mAnalisador de Triângulos\33[m')
print('\33[33m-=\33[m' * 14)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print(f'\33[30mCom as medidas de {a}, {b} e {c}\33[m, \33[32mÉ POSSÍVEL FORMAR UM TRIÂNGULO\33[m!')
else:
    print(f'\33[30mCom as medidas de {a}, {b} e {c}\33[m, \33[31mNÃO É POSSÍVEL FORMAR UM TRIÂNGULO\33[m!')
