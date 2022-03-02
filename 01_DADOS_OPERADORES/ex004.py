# Exercício Python 4: Faça um programa que:
# a) leia algo pelo teclado e mostre na tela o seu tipo primitivo;
# b) todas as informações possíveis sobre ele.

n = input ('Digite um numéro: ')

print (('O tipo primitivo desse valor é:'), type(n))
print ('É um número?', n.isnumeric())
print ('É um decimal exato?', n.isdecimal())
print ('Contem letra?', n.isalpha())
print ('É um digito?', n.isdigit())
print ('Contem somente espaços?', n.isspace())
