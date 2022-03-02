"""Exercício 79 – Valores únicos em uma Lista

A) Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
B) Caso o número já exista lá dentro, ele não será adicionado.
C) No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

numeros = []

while True:
    num = (int(input('Digite um valor: ')))
    if num not in numeros:
        numeros.append(num)
        print('> Número adicionado com sucesso! <')
    else:
        if num in numeros:
            print('> O número já contido na lista <')

    r = str(input('Deseja continuar? Digite [S/N]: ')).lower()

    while r not in 'SsNn':
        print(f'Caractere inválido, por favor tente novamente!')
        r = str(input('Deseja continuar? Digite [S/N]: ')).lower()

    if r == 'n':
        break

print(f'Os números  digitados válidos foram {sorted(numeros)}')
