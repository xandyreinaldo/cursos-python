n = (int(input('Digite um numero inteiro: ')))
print('''Escolha uma das bases para covensão:
[ 1 ] converter para numero BINÁRIO
[ 2 ] converter para numero OCTAL
[ 3 ] converter para numero HEXADECIMAL''')
escolhido = (int(input('sua opção: ')))
if escolhido == 1:
    print('{} convertido para BINARIO é igual a {}'.format(n, bin(n)[2:]))
elif escolhido == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif escolhido == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[:2]))
else:
    print('opção inválida, tente novamente')
