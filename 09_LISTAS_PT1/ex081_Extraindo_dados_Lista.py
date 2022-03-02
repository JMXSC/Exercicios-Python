'''Exercício 81 – Extraindo dados de uma Lista

A)Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
B) Quantos números foram digitados.
C) A lista de valores, ordenada de forma decrescente.
D) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
c = 0

while True:
    lista.append(int(input('Digite um número: ')))
    c += 1
    r = str(input('Deseja continuar? [S/N]: ')).lower()

    while r not in 'SsNn':
        print('Opção inválida, tente novamente!')
        r = str(input('Deseja continuar? [S/N]: ')).lower()

    if r == 'n':
        break

print(f'Ao total foram digitados {c} números') #ordem reversa lista... <ou usar len(lista)>
lista.sort(reverse=True)
print(f'Os valores digitados em ordem decresente foram: {lista}') #ordem reversa lista


if 5 in lista:
    print('O número 5 foi digitado e está na lista')
else:
    print('O número 5 não foi digitado')
