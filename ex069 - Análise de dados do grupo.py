""" 69 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """

m18 = h = mm20 = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA'.center(30))
    print('-'*30)
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-'*30)
    if i > 18:
        m18 += 1
    if s == 'M':
        h += 1
    if s == 'F' and i < 20:
        mm20 += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {m18}.
Ao todo, há {h} homens cadastrados.
E há {mm20} mulheres com menos de 20 anos.''')
