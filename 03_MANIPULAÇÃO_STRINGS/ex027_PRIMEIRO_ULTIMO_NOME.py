# Exercício Python 27: Faça um programa que:
# a) leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

n = input('Digite seu  nome completo: ').title().strip()

nome = n.split()
print('Prazer em te conhecer!')

print('Seu primeiro nome é: {}' .format(nome[0]))
print('Seu último nome é {}' .format(nome[len(nome)-1]))