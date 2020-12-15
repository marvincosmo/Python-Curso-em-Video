""" 08 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. """

m = float(input('Informe o valor, em metros (m): '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'{m} metros valem o mesmo que:')
print(f'{km} quilômetros;\n{hm} hectômetros;\n{dam} decâmetros;\n{dm} decímetros;\n{cm} centímetros ou;\n{mm} milímetros.')
