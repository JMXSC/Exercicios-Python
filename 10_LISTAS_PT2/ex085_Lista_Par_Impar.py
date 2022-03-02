'''Exercício 85 – Listas com pares e ímpares
A) Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única;
B) que mantenha separados os valores pares e ímpares.
C) No final, mostre os valores pares e ímpares em ordem crescente.'''

num = list()
par = list()
imp = list()
list_final = list()

for c in range(1, 8):
    num.append(int(input('Digite um valor: ')))

    for n in num:
        if n % 2 == 0:
            par.append(n)
        else:
            if n % 2 == 1:
                imp.append(n)
        num.clear()
    par.sort()
    imp.sort()
    list_final = [par, imp]

print(f"Lista contendo valores pares e impares separados e em ordem crescente: {list_final}")

''' 
Outra forma de resolver o problema

num = [[],[]]
valor  = 0
for c in range(1,8)
    valor = int(input('Digite o {c}° valor: ')
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(c)
num[0].sort()
num[1].sort()
print(f"Lista contendo valores pares e impares separados e em ordem crescente: {num}")'''
