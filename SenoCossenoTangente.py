import math
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
hi = math.hypot(co, ca)
seno = co/hi
cosseno = ca/hi
tangente = co/ca
print('Seno: {:.3f}'.format(seno))
print('Cosseno: {:.3f}'.format(cosseno))
print('Tangente: {:.3f}'.format(tangente))