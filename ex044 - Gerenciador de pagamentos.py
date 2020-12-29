""" 44 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros """

print(f"{' LOJAS CARIOCAS ':=^40}")
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista em dinheiro ou cheque
[ 2 ] à vista em cartão
[ 3 ] em 2x em cartão
[ 4 ] em 3x ou mais em cartão''')
opção = int(input('Selecione: '))
if opção == 1:
    valor = preço - preço * 10 / 100
    print('Essa opção dá 10% de desconto.')
elif opção == 2:
    valor = preço - preço * 5 / 100
    print('Essa opção dá 5% de desconto.')
elif opção == 3:
    valor = preço
    parcela = valor / 2
    print(f'A compra será feita em 2 parcelas de R${parcela:.2f}, SEM JUROS.')
elif opção == 4:
    vezes = int(input('Quantas parcelas? '))
    valor = preço + preço * 20 / 100
    parcela = valor / vezes
    print(f'A compra será feita em {vezes} parcelas de R${parcela:.2f}, COM JUROS.')
else:
    valor = preço
    print('Esta opção não existe. Escolha uma das opções acima.')
print(f'Sua compra de R${preço:.2f} vai custar R${valor:.2f}, no final')
