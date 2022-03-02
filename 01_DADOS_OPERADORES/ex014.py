# Exercício Python 14: Escreva um programa que:
# a) converta uma temperatura digitada em graus Celsius para graus Fahrenheit.

temp = float(input('Temperatura em C°: '))
convertF = temp * 1.8 + 32

print ('A temperatura de {:.1f} C° corresponde a {:.1f} F°' .format(temp, convertF))
