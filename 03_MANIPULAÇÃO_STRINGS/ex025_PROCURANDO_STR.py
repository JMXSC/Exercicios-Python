# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome completo: '))

s = 'Silva' in nome.title()
print('O nome tem Silva? {}' .format(s))
