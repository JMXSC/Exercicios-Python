'''Exercício 83 – Validando expressões matemáticas

A) Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
B) Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''


exp = str(input('Digite uma expressão matématica: '))
lista = []

for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
