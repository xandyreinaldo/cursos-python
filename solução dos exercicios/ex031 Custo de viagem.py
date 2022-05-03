a = float(input('qual a distacia da viagem '))
km = a * 0.50
km2 = a * 0.45
if a <= 200:
    print('o preço da passagem sera de R$:',km)
else:
    print('o preço da passagem sera de R$:',km2)