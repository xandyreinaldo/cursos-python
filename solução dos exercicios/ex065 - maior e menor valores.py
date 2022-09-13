
respota = 's'
media = soma = quantidade = maior = menor = 0
while respota in 'Ss':
    digitado = int(input("Digite um numero..."))
    soma += digitado
    quantidade += 1
    if quantidade == 1:
        maior = menor = digitado
    else:
        if digitado > maior:
            maior = digitado
        if digitado < menor:
            menor = digitado

    respota = str(input('quer continuar? '))
media = soma / quantidade

print('voce digitou {} numeros e a média foi de {}, o menor numeor digitado foi de {} e o meior foi {}'.format(quantidade, media, menor, maior))
