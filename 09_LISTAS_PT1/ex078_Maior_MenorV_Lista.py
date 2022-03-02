'''Exercício 78 – Maior e Menor valores na Lista

A) Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
b) Mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

valores = []

for num in range(1, 6):
    valores.append(int(input(f'Digite o {num}° valor: ')))


print(f'\nOs valores digitados foram {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições', end=' ')

for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end='')

print(f'\nO menor valor digitado foi {min(valores)} nas posições', end=' ')

for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end='')
