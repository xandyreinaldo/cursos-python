
num = int(input('Digite um Numero: '))
tot = 0
for n in range(1, num + 1):
    if num % n == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(n), end='')
print('\n\033[mo numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('esse numero é primo')
else:
    print('esse numero não é primo')