'''Exercício 76 – Lista de Preços com Tupla

A) Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
B) No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

compras = ('kindle', 400, 'echod', 180, 'ssd', 250,
           'fone', 20, 'capinha', 20, 'pelicula', 20,
           'livros', 100, 'tenis', 190, 'relogio', 70)

print('-' * 50)
print('\033[;7mLISTA DE COMPRAS\033[m'.center(55))
print('-' * 50)

for pos in range(0, len(compras)):
    if pos % 2 == 0:
        print(f'{compras[pos]:.<30}', end= '')
    else:
        print(f'R$ {compras[pos]:2}')
print('-' * 50)
