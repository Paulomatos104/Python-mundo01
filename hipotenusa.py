import math
ang = float(input("qual o angulo que você deseja ver: "))
seno = math.sin(math.radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, seno))
cos = math.cos(math.radians(ang))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, cos))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem o tangente de {:.2f}'.format(ang, tan))