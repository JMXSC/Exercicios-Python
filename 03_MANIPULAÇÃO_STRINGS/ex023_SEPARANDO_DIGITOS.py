# Exercício Python 23: Faça um programa que:
# a) leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = float(input('Digite um numero qualquer: '))

unidade = num // 1 % 10
dezena  = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('Anlisando o número {}, vejo que ele possui:' .format(num))
print('UNIDADES(S): {:.0f}' .format(unidade))
print('DEZENA(S): {:.0f}' .format(dezena))
print('CENTENA(S): {:.0f}' .format(centena))
print('MILHAR: {:.0f}' .format(milhar))