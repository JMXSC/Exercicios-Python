# Exercício Python 15: Escreva um programa que:
# a) pergunte a quantidade de Km percorridos por um carro alugado;
# b) a quantidade de dias pelos quais ele foi alugado;
# c) Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int (input('Quantos dias alugados: '))
km = float (input('KM rodados? '))
alug_dia = 60
km_dia = 0.15
preço = (dias * alug_dia) + (km * km_dia)

print('O total a pagar é: R$ {:.2F}' .format(preço))


