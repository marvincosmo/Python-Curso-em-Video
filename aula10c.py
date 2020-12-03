n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')
# print('Sua média foi boa! PARABÉNS' if m >= 6.0 else 'Sua média foi ruim! ESTUDE MAIS!')  <- Forma simplificada
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
