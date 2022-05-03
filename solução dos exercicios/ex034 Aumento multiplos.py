s = float(input('Qual é seu salario? '))
if s >= 1250.00:
    '''salario maior'''
    p = 10
    c = s + (s * 10 / 100)
else:
    '''salario menor'''
    p = 15
    c = s + (s * 15 / 100)
print('o salario com o aumento de {}% será de {:.2f}'.format(p, c))
