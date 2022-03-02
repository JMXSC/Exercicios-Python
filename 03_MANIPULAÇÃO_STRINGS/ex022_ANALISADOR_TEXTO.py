# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

# a) O nome com todas as letras maiúsculas e minúsculas.
# b) Quantas letras tem ao tod (sem considerar espaços).
# c) Quantas letras tem o primeiro nome.

frase = str(input('Digite seu nome: ')).strip()

print('Analisando o nome: {}'.format(frase.title()))

print('O nome possui um total de {} letras' .format(len(frase)-frase.count(' ')))

print('O NOME EM LETRAS MAIÚSCULAS FICA: {} ' .format(frase.upper()))

print('o nome em letras minúsculas fica: {} ' .format(frase.lower()))

print('O primeiro nome possui {} letras ' .format(len(frase.split()[0])))
