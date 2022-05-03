from sys import exit
from datetime import date
hm = int(input('[ 1 ] vocé é HOMEM \n[ 2 ] voce é MULHER: '))
if 2 == hm:
    print('o alistamento ñao é obrigatorio para MULHERES'), exit(0)
nas = int(input('digite seu ano de nascimento: '))
a = date.today().year - nas
b = 18 - a
c = a - 18
print('Quem nasceu em {} tem {}Anos em 2022.'.format(nas, a))
if a > 18:
    print('você ja deveria ter se alistado há {:} Anos,  seu alistamento foi em {}'.format(c, date.today().year - c))
elif a == 18:
    print('voce tem q se alistar IMEDIATAMENTE')
elif a < 18:
    print('Ainda faltam {} Anos para seu alistamento, seu alistamento sera em {}'.format(b, date.today().year + b))
