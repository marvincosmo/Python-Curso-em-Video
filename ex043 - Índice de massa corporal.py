""" 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida """

peso = float(input('Qual é o peso (Kg)? '))
altura = float(input('Qual é a altura (m)? '))
imc = peso / altura ** 2  # também pode escrever pow(altura, 2) ou altura * altura
print(f'''O IMC dessa pessoa é de {imc:.1f}.
Ela está''', end=' ')
if imc < 18.5:
    print('\033[34mabaixo do peso normal\033[m.')
elif 18.5 <= imc < 25:
    print('\033[32mno peso ideal\033[m.')
elif 25 <= imc < 30:
    print('\033[33mcom sobrepeso\033[m.')
elif 30 <= imc < 40:
    print('\033[35mcom obesidade\033[m.')
elif imc > 40:  # também pode escrever else:
    print('\033[31mcom obesidade mórbida\033[m.')

# Esta outra resposta foi criada pelo Marcos do futuro:
"""
while True:
    peso = float(input('Qual é o peso (Kg) [Digite 0 para parar]? '))
    if peso == 0:
        break
    altura = float(input('Qual é a altura (m) [Digite 0 para parar]? '))
    if altura == 0:
        break
    imc = peso / altura ** 2
    print(f'''O IMC dessa pessoa é de {imc:.1f}.
    Ela está''', end=' ')
    if imc < 18.5:
        print('\033[34mabaixo do peso normal\033[m.')
    elif 18.5 <= imc < 25:
        print('\033[32mno peso ideal\033[m.')
    elif 25 <= imc < 30:
        print('\033[33mcom sobrepeso\033[m.')
    elif 30 <= imc < 40:
        print('\033[35mcom obesidade\033[m.')
    elif imc > 40:
        print('\033[31mcom obesidade mórbida\033[m.')
print('Fim do programa.')
"""