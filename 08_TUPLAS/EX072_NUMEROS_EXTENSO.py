'''Exercício 72: Números por Extenso

A) Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
B) Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:

    escolha = int(input('Digite um número inteiro entre 0 e 20: '))

    for pos, num in enumerate(extenso):
     if pos == escolha:
        print(f'Você digitou o número -> {num}.')

    if escolha > 20:
        print('Erro, tente novamente!')
    elif escolha < 0:
        print('Erro, tente novamente!')
