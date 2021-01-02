""" 73 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
A) Apenas o 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense. """
# Minha resposta:
"""
print('-'*40)
print('Campeonato Brasileiro de Futebol 2019'.center(40))
print('-'*40)
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético Paranaense', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético Mineiro', 'Fluminense', 'Botafogo', 'Ceará',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print(f'Lista dos times: {times}')
print('-'*40)
print(f'Os 5 primeiros colocados: {times[:5]}')
print('-'*40)
print(f'Os 4 últimos colocados: {times[16:]}')
print('-'*40)
print(f'Os times, em ordem alfabética: {sorted(times)}')
print('-'*40)
print(f"Nesse ano, a Chapecoense ficou na {times.index('Chapecoense')+1}ª posição.")
"""
# Resposta do professor:
print('-'*40)
print('Campeonato Brasileiro de Futebol 2017'.center(40))
print('-'*40)
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
         'Atlético Mineiro', 'Botafogo', 'Atlético Paranaense', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético Goianiense')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
