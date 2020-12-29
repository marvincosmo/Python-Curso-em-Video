""" 59 - Crie um programa que leia dois valores e mostre um menu na tela:
 [ 1 ] somar
 [ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    op = int(input(' Qual é a sua opção? '))
    if op == 1:
        print(f'{a} + {b} = {a+b}')
    elif op == 2:
        print(f'{a} x {b} = {a*b}')
    elif op == 3:
        if a > b:
            maior = a
        else:
            maior = b
        print(f'O maior valor é {maior}.')
    elif op == 4:
        print('Informe os novos valores.')
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(1)
print('Fim do programa! Volte sempre!')
