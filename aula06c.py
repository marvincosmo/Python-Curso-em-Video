n = input('Digite algo: ')
print('O que você digitou...')
print(f'É de que tipo primitivo? {type(n)}')
print(f'É alfanumérico? {n.isalnum()}')
print(f'É alfabético? {n.isalpha()}')
print(f'É decimal? {n.isdecimal()}')
print(f'É formado por dígitos? {n.isdigit()}')
print(f'É um identificador? {n.isidentifier()}')
print(f'Está digitado com letras minúsculas? {n.islower()}')
print(f'É numérico? {n.isnumeric()}')
print(f'Pode ser impresso? {n.isprintable()}')
print(f'É um espaço em branco? {n.isspace()}')
print(f'Segue a regra de titulação? {n.istitle()}')
print(f'Está digitado com letras maiúsculas? {n.isupper()}')
