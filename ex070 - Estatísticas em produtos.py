""" 70 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """

print('-'*30)
print('LOJA LOGÍSTICA'.center(30))
print('-'*30)
t = m = c = b = 0
mb = ''
while True:
    n = str(input('Nome do produto: '))
    p = float(input('Preço: R$'))
    c += 1
    t += p
    if p > 1000:
        m += 1
    if c == 1:
        b = p
        mb = n
    else:
        if p < b:
            b = p
            mb = n
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
print('-'*10, 'FIM DO PROGRAMA', '-'*10)
print(f'''O total da compra foi de R${t:.2f}.
Há {m} produtos custando mais de R$1000.00.
O produto mais barato foi {mb}, que custa R${b:.2f}.''')
