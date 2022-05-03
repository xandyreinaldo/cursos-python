a = float(input('Largura da parede: '))
b = float(input('Altura da parede'))
c = a * b
tinta = c/2
print('Sua parede tem a dimensão de {}x{}, e sua área de {}m² \npara pintar essa parede, você precisará de {}L de tinta'.format(a, b, c,tinta))
