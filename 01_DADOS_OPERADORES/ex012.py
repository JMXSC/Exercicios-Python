# Exercício Python 12: Faça um algoritmo que:
# a) leia o preço de um produto;
# b) mostre seu novo preço, com 5% de desconto.

preço_prod = float(input('Preço do produto: R$ '))
desc = (preço_prod * 5 / 100)
prod_desc = preço_prod - desc

print ('O valor a ser pago pelo produto com 5% de desconto é: R$ {:.2f}' .format(prod_desc))
