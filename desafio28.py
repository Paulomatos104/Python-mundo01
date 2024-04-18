from random import *
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5! TENTE ADIVINHAR...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
if n == 5:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número 5 e não no {n}')