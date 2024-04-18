sal = float(input('Digite o salário do funcionário: R$'))
if sal <= 1250:
    aum = sal + (sal * 0.15)
    print(f"O novo saário do fundionário é {aum}")
else:
    aum = sal + (sal * 10)
    print(f"O novo salario do funcionário é {aum}")