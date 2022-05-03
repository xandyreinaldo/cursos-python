from random import shuffle
a = input('nome do primeiro aluno: ')
b = input('segundo aluno: ')
c = input('terceiro aluno: ')
d = input('quarto aluno: ')
lista = [a, b, c, d]
shuffle(lista)
print('a ordem apresentada sera...')
print(lista)
