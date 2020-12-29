""" 49 - Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que, agora, utilizando um
laço 'for'. """

print('\33[31m=\33[m' * 17, '\33[7;31mTABUADA\33[m', '\33[31m=\33[m' * 17)
n = int(input('\33[36mInforme um número para saber sua tabuada: \33[m'))
for m in range(1, 11):
    print(f'\33[37m{n} x {m:2} = {n*m}\33[m')
print('\33[36mPronto!\33[m')
