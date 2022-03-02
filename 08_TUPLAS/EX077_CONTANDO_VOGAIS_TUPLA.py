'''Exercício 77 – Contando vogais em Tupla

A) Crie uma tupla com várias palavras (não usar acentos).Depois disso, mostre:
B) para cada palavra, quais são as suas vogais.'''

palavras = ('notebook', 'livro', 'mouse', 'musica', 'comida',
            'headset', 'estudar', 'lembrar', 'ler', 'sair')

for p in palavras:
    print(f'\nNa palavra <{p.upper()}> temos: ', end= '')
    for letra in p:
     if letra in"aeiou":
        print(letra, end= ' ')
