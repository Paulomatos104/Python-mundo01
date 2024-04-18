num = input('Escreva um número até 9999: ')
tam = len(num)

if tam == 1:
    print(f'Unidade: {num}')
    print('Dezena: 0')
    print('Centena: 0')
    print('Milhar: 0')
elif tam == 2:
    print(f'Unidade: {num[-1:]}')
    print(f'Dezena: {num[-2:-1]}0')
    print('Centena: 0')
    print('Milhar: 0')
elif tam == 3:
    print(f'Unidade: {num[-1:]}')
    print(f'Dezena: {num[-2:-1]}0')
    print(f'Centena: {num[-3:-2]}00')
    print('Milhar: 0')
elif tam == 4:
    print(f'Unidade: {num[-1:]}')
    print(f'Dezena: {num[-2:-1]}0')
    print(f'Centena: {num[-3:-2]}00')
    print(f'Milhar: {num[-4:-3]}000')
else:
    print("Número inválido. Digite um número até 9999.")
