# from math import sin, cos, tan, radians
import math
a = float(input('Digite um ângulo que você deseja: '))
b = math.sin(math.radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, b))
c = math.cos (math.radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, c))
d = math.tan(math.radians(a))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(a,d))