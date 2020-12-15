""" 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode
comprar. """

brl = float(input('Quanto dinheiro você tem na carteira? R$'))
usd = brl / 5.65
eur = brl / 6.62
ars = brl / 0.073
jpy = brl / 0.054
inr = brl / 0.077
rub = brl / 0.073
print(f'Com R${brl:.2f}, você pode comprar:\nUS${usd:.2f};\n€{eur:.2f};\n${ars:.2f} (pesos argentinos);\n¥{jpy:.2f};\n₹{inr:.2f};\n₽{rub:.2f}')
