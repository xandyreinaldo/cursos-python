a = int(input('Digite um numero'))
b = int(input('Digite mais um numero'))
c = int(input('digite mais um numero'))
#verificar menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    nenor = c
#verificar maio
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))