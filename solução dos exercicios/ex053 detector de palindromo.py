frase = input('Digite uma frase:').strip().upper()
palavras = frase.split()
tudo = ''.join(palavras)
inverso = tudo[::-1]
'''inverso = ''
for letra in range(len(tudo) -1, -1, -1):
    inverso += tudo[letra]'''
if inverso == tudo:
    print('temos um palindromo!')
else:
    print('a frase digitada não é um palindromo')
print(tudo, inverso)
