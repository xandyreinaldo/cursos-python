from time import sleep
casa = float(input('qual o valor da cassa? '))
salario = float(input('Qual é o seu salario? '))
anos = int(input('Em quantos anos quer pagar? '))
s = (salario * 30 / 100) #30%
mes = anos * 12 #anos
prest = casa / mes #prestação
print('Processando...')
sleep(3)
if s >= prest:
    print('\033[1;36memprestimo aprovado, parabéns...\033[m')
    print('\033[1;36ma sua prestação sera de R$:{:.2f}\033[m'.format(prest))
else:
    print('\033[1;31memprestimo foi negado, sinto muito \033[m')
    print('\033[1;31mpara pagar um empretimo de R$:{:.2f} em {}anos, a sua prestação seria de R$:{:.2f} \033[m'.format(casa,anos, prest))
