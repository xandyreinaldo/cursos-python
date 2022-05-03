print('-=-'*15)
a = int(input('Primeiro valor: '))
b = int(input('Segundo Valor: '))
c = 0
while c != 5:
    print('''    [1] Soma
    [2] Multiplica
    [3] Maior
    [4] Novos numeros
    [5] Sair do Programa''')
    c = int(input('Qual sua opção?: '))
    if c == 1:
        soma = a + b
        print('a soma de {} + {} = {}'.format(a, b, soma))
    elif c == 2:
        multiplica = a * b
        print('a multiplicação de {} x {} = {}'.format(a, b, multiplica))

    elif c == 3:
        if a > b:
            print('o maior numero foi', a)
        else:
            print('o maior numero foi', b)

    elif c == 4:
        print('informe os numeros novamentes: ')
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo Valor: '))
    elif c == 5:
        print('finalizando')
    else:
        print('opção invalida. Tente novamente')
    print('-=-' * 15)
print('fim do programa')
