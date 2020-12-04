""" 36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado."""

imóvel = float(input('Qual é o valor do imóvel? R$'))
salário = float(input('Qual é o salário do comprador? R$'))
tempo = int(input('Em quanto tempo o comprador pretende pagar o empréstimo? '))
prestação = imóvel / (tempo*12)
print(f'Para pagar um imóvel de R${imóvel:.2f} em {tempo} anos, a prestação mensal será de R${prestação:.2f}.')
if prestação > salário * 30 / 100:
    print('Empréstimo \033[31mNEGADO!\033[m')
else:
    print('Empréstimo \033[32mAPROVADO!\033[m')
'''
final da resposta elaborada pelo professor:
mínimo = salário * 30 / 100
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
'''
