idademaior = 0
mediaidade = 0
idadeH = 0
idadeHV = ''
m20 = 0
for nome1 in range(1, 5):
    nome = input('nome da {}ª pessoa: '.format(nome1)).strip()
    idade = int(input(' Qual é a sua idade?: '))
    sexo = str(input('Qual é o seu sexo ( M ) (F)')).strip()
    print('--'*15)
    idademaior += idade
    if nome1 == 1 and sexo in 'Mm':
        idadeH = idade
        idadeHV = nome
    if sexo in 'Mm' and idade > idadeH:
        idadeH = idade
        idadeHV = nome
    if sexo in 'Ff' and idade < 20:
        m20 += 1
mediaidade = idademaior / 4
print('a media de idade do grupo é {} anos'.format(mediaidade))
print('o homem mais velho tem {} anos, e se chama {}'.format(idadeH, idadeHV))
print('ao todo são {} mulhes com menos de 20 anos'.format(m20))
