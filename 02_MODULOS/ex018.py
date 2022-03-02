# Exercício Python 18: Faça um programa que:
# a) leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite o valor do ângulo: '))

print('Dado o ângulo {} o valor do SENO é: {:.2f}' .format (ang, math.sin(math.radians(ang))))

print('COSCENO: {:.2f}' .format(math.cos(math.radians(ang))))

print('TANGENTE: {:.2f}' .format(math.tan(math.radians(ang))))


