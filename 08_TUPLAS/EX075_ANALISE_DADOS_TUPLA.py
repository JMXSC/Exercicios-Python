''' Exercício 75 – Análise de dados em uma Tupla

A)Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
B) Quantas vezes apareceu o valor 9.
C) Em que posição foi digitado o primeiro valor 3.
D) Quais foram os números pares.'''

num = (int(input(f'Digite o 1° valor: ')),
      int(input(f'Digite o 2° valor: ')),
      int(input(f'Digite o 3° valor: ')),
      int(input(f'Digite o 4° valor: ')),
      int(input(f'Digite o 5° valor: ')))

print(f'\nOs valores digitados foram: {num}',
      f'\nO número 9 foi digitado {num.count(9)} vezes.')

if 3 in num:
 print(f'O número 3 apareceu pela primeira vez na {num.index(3)+1}° posição.')
else:
 print('O número 3 não foi digitado.')
print(f'Os números pares digitados foram: ', end= '- ')
for n in num:
    if n % 2 == 0:
     print(n, end= ' - ')
