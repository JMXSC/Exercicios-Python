# Exercício Python 11: Faça um programa que sabendo que cada litro de tinta pinta uma área de 2 metros²:
# a) leia a largura e a altura de uma parede em metros;
# b) calcule a sua área e a quantidade de tinta necessária para pintá-la.

largura_m2 = float(input('Largura: '))
altura_m2 = float(input('Altura: '))
area = largura_m2 * altura_m2
tinta = area / 2

print ('O valor total da área é: {}m²\nA quantidade de tinta necessária para pintar toda a área será: {} litros.' .format(area, tinta))
