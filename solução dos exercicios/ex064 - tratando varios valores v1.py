n = 0
contador = 0
soma = 0
n = int(input('Digite um numero [999 para parar}'))
while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um numero [999 para parar}'))
print('voce digitou {} numeros e a soma entre eles foi {}'.format(contador, soma))
