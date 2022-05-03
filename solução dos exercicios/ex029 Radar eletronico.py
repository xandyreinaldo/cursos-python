carro = float(input('qual é a velocidade do carro?? '))
multa = (carro-80) * 7
if carro < 80:
    print('parabéns, tenha um bom dia.... e dirija com segurança')
else:
    print('vc foi Multado, o limete maximo da via é 80km, a valor da multa é de R$: {:.2f}'.format(multa))