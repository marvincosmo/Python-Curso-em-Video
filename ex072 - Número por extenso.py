""" 72 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. """

números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        else:
            print('Tente novamente. ', end='')
    print(f'Você digitou o número {números[n]}.')
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
