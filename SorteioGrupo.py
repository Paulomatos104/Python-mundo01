import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
print('A ordem de aprensentação é: ')
alunos = [n1, n2, n3, n4]

# Sorteando 4 nomes sem substituição
ganhadores = random.sample(alunos, 4)

# Definindo a função do contador
def contador():
    # Loop de 1 até 4
    for i in range(1, 5):
        # Imprime o número atual e o ganhador correspondente
        print(f'{i}. {ganhadores[i-1]}')

# Chamando a função do contador
contador()
