from datetime import date
list = 0
menor = 0
for ano in range(1, 8):
    n = int(input('em que ano a {}ª pessoal nascel?: '.format(ano)))
    idade = date.today().year - n
    if idade >= 18:
        list += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(list))
print('e tambem tivemos {} pessoas mrnors se idade'.format(menor))
