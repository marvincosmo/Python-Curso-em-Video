""" 51 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão. """

print('=' * 30)
print(f"{'10 PRIMEIROS TERMOS DA PA':^30}")
print('=' * 30)
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + 1, razão):
    print(f'{c}', end=' → ')
print('ACABOU')
