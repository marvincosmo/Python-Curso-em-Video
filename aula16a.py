"""
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# Tuplas são imutáveis
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])
"""

lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')


for comida in lanche:
    print(f'Eu vou comer {comida}!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

print(sorted(lanche))

print(lanche)
