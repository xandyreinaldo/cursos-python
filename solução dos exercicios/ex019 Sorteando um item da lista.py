from random import choice
a = input('nome do primeiro aluno: ')
b = input('segundo aluno: ')
c = input('terceiro aluno: ')
d = input('quarto aluno: ')
list = [a, b, c, d]
'''escolhido = choice(list)'''
print('o aluno escolhido foi {}'.format(choice(list)))

