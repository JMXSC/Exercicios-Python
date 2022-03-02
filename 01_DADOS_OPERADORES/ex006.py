# Exercício Python 006: Crie um algoritmo que:
# a) leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número inteiro: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print ('O dobro desse número é: {} \nO triplo desse número é: {} \nA raiz desse número é: {:.2f}' .format (dobro, triplo, raiz))
