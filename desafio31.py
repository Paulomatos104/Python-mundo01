km = float(input('Qual a distância da viagem? '))
if km <= 200:
   valor = km * 0.50
   print(f'O valor da sua viagem deu {valor:.2f}')
else:
   valor = km * 0.45
   print(f'O valor da sua viagem deu {valor:.2f}')