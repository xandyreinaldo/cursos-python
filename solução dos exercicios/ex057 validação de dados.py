mf = str(input('Informe seu sexo: [ M, F]')).strip().upper()[0]
while mf not in 'MmFf':
    mf = str(input('dados invalidos, favor informe novament: ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(mf))
