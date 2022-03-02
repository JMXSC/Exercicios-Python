# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que:
# a) ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
a1 = input('Primeiro auluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input ('Quarto aluno: ')

lista = [a1, a2, a3, a4]
choice(lista)

print('O aluno escolhido foi: {}' .format(choice(lista)))
