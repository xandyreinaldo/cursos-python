print('Gerador de PA')
print('-=-'*15)
a = int(input('Primeirp Termo: '))
b = int(input('Razão da PA: '))
c = a
d = 1
total = 0
repet = 10
while repet != 0:
    total = total + repet
    while d <= total:
        print('{} -'.format(c), end='')
        c += b
        d += 1
    print('PAUSA')
    repet = int(input('quanto termos vc quer mostrar agora?: '))
print('progreção finalizada com {} termos mostrados '.format(total))
print('FIM')
