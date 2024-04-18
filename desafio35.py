print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('                 ANALISADOR DE TRIÂNGULO                  ')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
n1 = float(input('Escreva o valor da primeira reta: '))
n2 = float(input('Escreva o valor da segunda reta: '))
n3 = float(input('Escreva o valor da terceira reta: '))

if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    print('Os valores digitados PODEM formar um triângulo')
else:
    print('Os valores digitados NÃO PODEM formar um triângulo')    
#cor do terminal
#\033[1;31;43m 
