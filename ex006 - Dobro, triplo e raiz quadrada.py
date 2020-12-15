""" 06 - Crie um algoritmo que lei um número e mostre o seu dobro, triplo e raiz quadrada. """

n = int(input('Informe um número: '))
d = n * 2
t = n * 3
rq = n ** (1 / 2)  # também pode ser escrito como pow(n, (1/2))
print(f'O dobro de {n} é {d}, o triplo é {t}, e sua raiz quadrada é {rq:.2f}.')
