# Exercício Python 7: Desenvolva um programa que:
# a) leia as duas notas de um aluno, calcule-os e mostre a sua média.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

print ('O resultado da nota média desse aluno é: {:.2f}' .format (media))
