print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = int(input('quantos termos vc quer mostrar? '))
termo1 = 0
termo2 = 1
print('-'*30)
print('{} -> {}'.format(termo1, termo2), end="")
contador = 3
while contador <= n:
    termo3 = termo1 + termo2
    print(' -> {}'.format(termo3), end="")
    termo1 = termo2
    termo2 = termo3
    contador += 1
print(' ->fim')
print('-'*30)

