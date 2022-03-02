# Exercício Python 17: Faça um programa que:
# a) leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# b) Calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

print('O valor da hipotenusa é: {:.2f}' . format (hypot(co, ca)))
