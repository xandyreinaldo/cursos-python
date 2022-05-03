a = int(input('digite um numero inteiro: '))
b = int(input('digite mais um numero inteiro:'))
if a > b:
    print('o primeiro numero maior é {} \ne o {} é o segundo valor é'. format(a, b))
elif b > a:
    print('o segundo numero maior é {} \ne o {} é o segundo valor é'.format(b, a))
elif a == b:
    print('não existe valor maior, os dois numeros são iguais')