a = int(input('Digite um numero para calcular seu fatorial: '))
b = a
f = 1
print('Calculando {}! = '.format(a), end='')
while b > 0:
    print('{} '.format(b), end='')
    print(' x ' if b > 1 else ' = ', end='')
    f *= b
    b -= 1
print(f)



'''from math import factorial
a = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(a)
print('o fatotial de  {} é {}.'.format(a, f))'''

