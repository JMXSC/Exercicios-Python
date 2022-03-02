"""Exercício 80 – Lista ordenada sem repetições

A) Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista;
B) Já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

numeros = []

for c in range(0, 5):
    num = int(input(f'Digite um valor: '))

    if c == 0 or num > numeros[-1]: # verificando o primeiro e último valor da lista.
        numeros.append(num)
    else:
        pos = 0
        while pos < len(numeros): # organizando os valores
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                break
            pos += 1

print(f'Os valores digitados em ordem foram {numeros}')
