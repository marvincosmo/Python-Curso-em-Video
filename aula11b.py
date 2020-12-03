a = 3
b = 5
print(f'Os valores são \033[32;44m{a}\033[m e \033[31;44m{b}\033[m.\n')
nome = 'Guanabara'
print(f'Olá! Muito prazer em te conhecer, \033[4;34m{nome}\033[m\n')
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print(f"Olá! Muito prazer em te conhecer, {cores['pretoebranco']}{nome}{cores['limpa']}!")
