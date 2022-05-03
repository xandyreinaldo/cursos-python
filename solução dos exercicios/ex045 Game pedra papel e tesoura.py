from time import sleep
from random import randint
print('suas opções: ')
print('[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESPURA')
a = int(input('QUAL É SUA ESCOLHA:'))
list = ['pedra', 'papel', 'tesoura']
pc = randint(0, 2)
print('jo.....')
sleep(1)
print('ken....')
sleep(1)
print('Pooooooooooooooo!...')
sleep(1)
print('-=-'*20)
print('o computador escolheu {}'.format(list[pc]))
print('jogador jogou {}'.format(list[a]))
print('-=-'*20)
if pc == 0:
    if pc == a:
        print('\033[31mEMPATE')
    if pc == 1:
        print('\033[31mjogador vence')
    elif pc == 2:
        print('\033[31mvc perdeu')
    else:
        print('\033[3mjogada invalida')
elif pc == 1:
    if pc == 0:
        print('\033[31mvc perdeu')
    elif pc == 2:
        print('\033[31mjogador vence')
    else:
        print('\033[31mjogada invalida')
elif pc == 2:
    if pc == 0:
        print('\033[31mvc perdeu')
    elif pc == 1:
        print('\033[31mjogador vence')
    else:
        print('\033[31mjogada invalida')
