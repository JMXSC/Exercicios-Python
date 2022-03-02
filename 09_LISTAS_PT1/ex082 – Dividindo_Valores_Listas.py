'''Exercício 82 – Dividindo valores em várias listas
A) Crie um programa que vai ler vários números e colocar em uma lista.
B) Crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
C) Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
listap = []
listai = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)

    if num % 2 == 0:
        listap.append(num)
    else:
        listai.append(num)

    resp = str(input('Deseja continuar? [S/N]: ')).lower()

    while resp not in 'SsNn':
        print('Opção inválida, tente novamente!')
        resp = str(input('Deseja continuar? [S/N]: '))

    if resp == 'n':
        break

print(f'Lista contendo todos os números digitados: {lista}')
print(f'Os números pares digitados foram: {listap}')
print(f'Os números impares digitados foram: {listai}')
