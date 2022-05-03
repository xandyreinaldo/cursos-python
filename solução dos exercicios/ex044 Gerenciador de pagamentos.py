print('{:=^40}'.format(' Lojas de teste '))
a = float(input('qual o valor do produto?: '))
print('[ 1 ] valor a vista / cheque \n[ 2 ] valor à vista no catão \n'
      '[ 3 ] Em 2x no ncartão \n[ 4 ] 3x ou mais no cartão')
pg = int(input('Qual é a forma de pagamento? '))
if pg == 1:
    p10 = a - (a * 10 / 100)
    print('o valor total com desconto de 10% é de R$: {:.2f}'.format(p10))
elif pg == 2:
    p5 = a - (a * 5 / 100)
    print('o valor total a ser pago com 5% de desconto é de R$: {:.2f}'.format(p5))
elif pg == 4:
    par = int(input('quantas parcelas?: '))
    x3 = a + (a * 20 / 100)
    print('o valor das pacelas sera de R$: {} '.format(x3 / par))
    print('o valor total a ser pago com acrecimo de 20% é de {:.2f}'.format(x3))
elif pg == 3:
    print('o valor total a ser pago e sem desconto é de R$:', a)
else:
    pg = 0
    print('\033[31mcomando invalido tente novamente...')
