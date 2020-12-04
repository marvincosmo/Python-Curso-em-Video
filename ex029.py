""" 29 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar os 80 km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada quilômetro acima do limite. """

v = float(input('Qual é a velocidade atual do carro, em Km/h? '))
if v > 80:
    print(f'\33[31;7mMULTADO!\33[m', end=' ')
    print(f'\33[31mVocê excedeu o limite permitido, que é de 80Km/h.\nO valor da multa será \33[m', end='')
    print(f'\33[32mR${(v - 80) * 7:.2f}\33[m', end='')
    print('\33[31m!\33[m')
else:
    print('\33[34mVocê é um motorista exemplar!\33[m')
print('\33[96mTenha um bom dia! Dirija com segurança!\33[m')
