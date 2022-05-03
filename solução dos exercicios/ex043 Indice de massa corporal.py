peso = float(input('Qual é o seu pesso?: (Kg) '))
alto = float(input(' qual é sua altura?: (m) '))
imc = peso / (alto ** 2)
print('IMC dessa pessoa é de {:.1f}'.format(imc))
if 18 <= imc < 25:
    print('\033[31mPeso ideal')
elif imc < 18.5:
    print('\033[31mabaixo do pesso')
elif 25 <= imc < 30:
    print('\033[31msobrepeso')
elif 30 <= imc < 40:
    print('\033[31mObesidade')
else:
    print('\033[31mObsidade Mórbida')
