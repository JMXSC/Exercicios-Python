"""Exercício 84 – Lista composta e análise de dados
A)Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
B) Quantas pessoas foram cadastradas.
C) Uma listagem com as pessoas mais pesadas.
D) Uma listagem com as pessoas mais leves."""

p = list()
nomes = list()
mai = list()
men = list()
cont = 0

while True:
    nomes = input('Nome: ')
    p = int(input('Peso: '))

    if p > 80:
        mai.append(nomes)
        mai.append(p)
    if p <= 80:
        men.append(nomes)
        men.append(p)

    cont += 1
    resp = str(input('Deseja continuar? [S/N] ')).lower()

    while resp not in 'SsNn':
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
        resp = str(input('Deseja continuar? [S/N] ')).lower()

    if resp == 'n':
        break

print(f'Ao total fora cadastradas {cont} pessoas.\n')
print(f'listagem com as pessoas mais pesadas:\n')
print('-' * 15)

for pos in range(0, len(mai)):

    if pos % 2 == 0:
        print(f'{mai[pos]}', end=' com ')
    else:
        print(f'{mai[pos]:2}Kg')

print('-' * 15)
print()
print(f'listagem com as pessoas mais leves:\n')
print('-' * 15)

for pos in range(0, len(men)):

    if pos % 2 == 0:
        print(f'{men[pos]}', end=' com ')
    else:
        print(f'{men[pos]:2}Kg')
print('-' * 15)
