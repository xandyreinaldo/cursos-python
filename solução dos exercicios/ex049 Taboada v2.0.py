n = int(input('Escolha um Numero: '))
print('-=-'*5)
for a in range(1, 11):
    print('{} x {:2} = {:2}'.format(n, a, (n * a)))
print('-=-' * 5)
