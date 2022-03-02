# Exercício Python 5: Faça um programa que:
# a) leia um número Inteiro e mostre na tela o seu sucessore seu antecessor.

n = int(input('Digite um número inteiro: '))
antecessor = n - 1
sucessor = n + 1

print('Analisando o valor {} o seu antecessor é: {} e o seu sucessor é: {} ' .format(n, antecessor, sucessor))
