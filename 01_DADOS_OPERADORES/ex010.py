# Exercício Python 10: Crie um programa que:
# a) leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Digite um valor: R$ '))
dolar = carteira / 5.62

print ('Valor convertido em dolar: $ {:.2f}' .format(dolar))
