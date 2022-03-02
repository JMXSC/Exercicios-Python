# Exercício Python 26: Faça um programa que:
# a) leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”
# b) Em que posição ela aparece a primeira vez
# c) Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra (A) aparece {} vezes na frase' .format(frase.count('A')))

print('Aparece pela primeira vez na posição: {}' .format(frase.find('A')+1))

print('Aparece pela ultima vez vez na posição: {}' .format(frase.rfind('A')+1))
