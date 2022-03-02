# Exercício Python 30: Crie um programa que:
# a) leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

linha = ' ' * 60

number = int(input('Digite um número inteiro: '))
print(linha)

resultado = number % 2
if resultado == 0:
    print('O número {} é PAR.'.format(number))
else:
    print('O numero {} é IMPAR.'.format(number))
