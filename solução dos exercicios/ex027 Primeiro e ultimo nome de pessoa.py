n = str(input('Digite seu nome completo: ')) .strip()
nome = n.split()
print(' ola seja bem vindo....')
print('Seu primeiro nome é {}'.format(nome[0]))
print(' seu ultimo nome é {}'.format(nome[len(nome)-1]))
