#Descobrir o menor e maior número digitado
n1 = int(input('Escreva o Primeiro numero: '))
n2 = int(input('Escreva o Segundo numero: '))
n3 = int(input('Escreva o Terceiro numero: '))
#Descobrir maior número digitado
if n1 > n2 and n1 > n3:
    print(f'O maior número foi {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número foi {n2}')
else:
    print(f'O maior número foi {n3}')
#descobrir menor número digitado
if n1 < n2 and n1 < n3:
    print(f'O Menor número foi {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O Menor número foi {n2}')
else:
    print(f'O Menor número foi {n3}')

