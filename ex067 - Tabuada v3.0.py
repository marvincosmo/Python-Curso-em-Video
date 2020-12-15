""" 67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
usuário. O programa será interrompido quando o número solicitado for negativo. """

while True:
    n = int(input('Informe um número para ver sua tabuada: '))
    if n < 0:
        break
    print('-' * 13)
    for m in range(1, 11):
        print(f'{n} x {m} = {n*m}')
    print('-' * 13)
print('Programa encerrado.')
