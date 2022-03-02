# Exercício Python 13: Faça um algoritmo que:
# a) leia o salário de um funcionário;
# b) mostre seu novo salário, com 15% de aumento.

sal_func = float(input('Salário atual: R$ '))
aumento = (sal_func * 15 / 100)
sal_aumento = sal_func + aumento

print ('O valor do salário com aumento de 15% será: R$ {:.2f}' .format(sal_aumento))
