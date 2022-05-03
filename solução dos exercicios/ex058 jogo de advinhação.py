from random import randint
pc = randint(0, 10)
print('Sou seu computador... \nAcabei de pensar em um numero entre 0 e 10 \nSerá que vc vonsegue adivinhar?')
acertou = False
palpite = 0
while not acertou:
    num = int(input('qual é o seu palpite?: '))
    palpite += 1
    if num == pc:
        acertou = True
    else:
        if num < pc:
            print('mais... tente mais uma vez.')
        elif num > pc:
            print('menos... tente mais uma vez.')
print('parabéns vc acertou')
print('Acertou com {} tentativas'.format(palpite))
