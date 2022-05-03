a = int(input('Digete aki seu numero: '))
u = a // 1 % 10
d = a // 10 % 10
c = a // 100 % 10
m = a // 1000 %10
print('a unidade é {}'.format(a))
print('a dezena é {}'.format(d))
print('centena é {}'.format(c))
print('milhar {}'.format(m))