from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um numero, entre 1 e 5. Tente adivinhar')
print('-=-'*20)
a = randint(0,5)
b = int(input('Em que numero eu pensei??'))
print(('processando....'))
sleep(4)
if b == a:
    print('parabéns vc acertou')
else:
    print('eu pensei em {} ,não foi dessa vez.... tente novamente'.format(a))
