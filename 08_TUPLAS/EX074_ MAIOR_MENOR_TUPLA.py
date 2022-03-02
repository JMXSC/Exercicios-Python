'''Exercício 74 - Maior e menor valores em Tupla:

a) Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso:
b) Mostre a listagem de números gerados
c) Indique o menor e o maior valor que estão na tupla.'''

from random import randint

num = (randint(1,100), randint(1,100), randint(1,100),
       randint(1,100), randint(1,100))

print(f'Os valores sorteados foram: ', end='')
for n in num:
 print(f'{n}', end=' ')

print(f'\nO menor número na tupla é: {min(num)}')
print(f'O maior número na tupla é: {max(num)}')
