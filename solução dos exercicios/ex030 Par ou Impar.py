from time import sleep
print('-=-'*20)
print('Par ou Impar')
print('-=-'*20)
a = int(input('Digite um numero: '))
resultado = a % 2
print('LOARDING.....')
sleep(2)
if resultado:
    print('esse numero é impar')
else:
    print('esse numero é par')
