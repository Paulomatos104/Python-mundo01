#Ler uma frase e dizer quantas vezes a letra “A” aparece, em que posição a primeira letra “A” aparece, e em qual posição a ultima aparece
Text1 = input('Escreva uma frase: ').upper()
print(f'O "A" aparece {Text1.count('A')} ')
print(f'A primeira letra "A" apareceu na {Text1.find('A')+1}')
print(f'A ultima letra "A" na posição {Text1.rfind('A')+1}')



