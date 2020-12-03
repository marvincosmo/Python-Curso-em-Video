r = 'S'
while r in 'Ss':  # outra opção aqui é while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] '))  # Mas aí tem que colocar o .upper() aqui.
print('Fim')
