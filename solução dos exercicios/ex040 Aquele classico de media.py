from time import sleep

nota1 = float(input('primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Loarding.......')
sleep(2)
print('tiradno a nota {} e a nota {}'.format(nota1, nota2))
if media >= 7.0:
    print('com a media {:.2} , vc foi \033[0:32mAPROVADO, PARABÉNS....'.format(media))
elif 7 > media >= 5:
    print('com a media {}, vc está de \033[0:33mRECUPERAÇÃO'.format(media))
elif media < 4.9:
    print('com a media {}, vc esta \033[0:31mREPROVADO'.format(media))
