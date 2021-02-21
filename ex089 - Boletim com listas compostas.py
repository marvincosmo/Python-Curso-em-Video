""" 89 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente. """

aluno = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    aluno.append([nome, [nota1, nota2], media])
    r = str(input('Gostaria de continuar [S/N]? ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 30)
print(f"{'Nª':<4}{'Nome':<15}{'Média':>8}")
print('-' * 30)
for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<15}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    o = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if o == 999:
        print('Finalizando...')
        break
    if o <= len(aluno) - 1:
        print(f'As notas de {aluno[o][0]} são {aluno[o][1]}')
print('<<< VOLTE SEMPRE >>>')
