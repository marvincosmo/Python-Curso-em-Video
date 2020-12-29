""" 37 - Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. """

n = int(input('Informe um número inteiro qualquer: '))
r = int(input('''Para qual base será convertido o número?
[ 1 ] - Binário
[ 2 ] - Octal
[ 3 ] - Hexadecimal
Selecione: '''))
if r == 1:
    print(f'O número {n} convertido para Binário é igual a {bin(n)[2:]}.')
elif r == 2:
    print(f'O número {n} convertido para Octal é igual a {oct(n)[2:]}.')
elif r == 3:
    print(f'O número {n} convertido para Hexadecimal é igual a {hex(n)[2:]}.')
else:
    print('Esta opção não existe.')

# Esta outra resposta foi criada pelo Marcos do futuro:
"""
while True:
    n = int(input('Informe um número inteiro qualquer: '))
    if n == 0:
        break
    r = int(input('''Para qual base será convertido o número?
    [ 1 ] - Binário
    [ 2 ] - Octal
    [ 3 ] - Hexadecimal
    Selecione: '''))
    if r == 1:
        print(f'O número {n} convertido para Binário é igual a {bin(n)[2:]}.')
    elif r == 2:
        print(f'O número {n} convertido para Octal é igual a {oct(n)[2:]}.')
    elif r == 3:
        print(f'O número {n} convertido para Hexadecimal é igual a {hex(n)[2:]}.')
    else:
        print('Essa opção não existe. Tente novamente')
print('Fim do programa.')
"""