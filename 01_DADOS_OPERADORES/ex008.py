# Exercício Python 8: Escreva um programa que:
# a) leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000

print ('O valor em centimetros é: {} cm \nO valor em milimetros é: {} mm' .format (centimetros, milimetros))
