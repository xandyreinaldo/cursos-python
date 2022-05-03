from datetime import date
ano = int(input('Digite seu Ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('com {} Anos, sua Classificação é \33[0:31mMIRIM'.format(idade))
elif 14 >= idade >= 10:
    print('com {} Anos, sua classificação é \033[0:31mINFANTIL'.format(idade))
elif 19 >= idade >= 15:
    print('com {} Anos, sua classificação é \033[0:31mJÚNIOR'.format(idade))
elif 25 >= idade >= 20:
    print('com {} Anos, sua classificação é \033[0:31mSÊNIOR'.format(idade))
else:
    print('com {} Anos, sua classificação é \033[0:31mMASTER'.format(idade))
