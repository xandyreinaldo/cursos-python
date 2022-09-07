print('Gerador de PA')
print('-=-'*15)
a = int(input('Primeirp Termo: '))
b = int(input('Razão da PA: '))
c = a
d = 1
while d <= 10:
    print('{} -'.format(c), end = '')
    c += b
    d+=1
print('fim')