# Exercício Python 28: Escreva um programa que:
# a) faça o computador “pensar” em um número inteiro entre 0 e 5
# b) Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# OBS: O programa deverá escrever na tela se o usuário venceu ou perdeu.

# PASSO 1 - ENUNCIADO

linha = '\033[1;37m*\033[m' * 60
frase = '\033[1;33mBEM-VINDO(A) AO JOGO DA ADIVINHAÇÃO\033[m'

print(linha)

print(frase.center(70))

print(linha)

linha1 = ' ' * 60

print(linha1 * 2)

# PASSO 2 - CONHECENDO O JOGADOR

nome = input('\033[1;37m- Oi, Qual o seu nome?\033[m ').strip().title()

linha1 = (' ') * 60

print(linha1 * 2)
print('Olá!! Boas vindas, {}. Meu nome é Alú,fico muito feliz em te conhecer, Vamos jogar? '.format(nome))
print(linha1 * 2)

# PASSO 3 - INICIANDO O JOGO

linha2 = (' ') * 50
linha2_1 = (' ') * 45
frase21 = 'FIM DE JOGO.'

while True:
    inicio = float(input('\033[33m>>>\033[m \033[1;31;47mDigite (1) SIM ou (0) NÃO:\033[m '))

    if inicio == 1:
        print('- Ótima escolha {}, vamos começar...'.format(nome))
        print(linha2 * 2)
        break
        print('OPÇÃO INVALIDA')

print(linha2 * 2)

from random import randint

IA = randint(0, 5)

linha3 = ('\033[1;33m*\033[m') * 60
linha3_1 = (' ')
frase3 = ('\033[1;33mEu Vou pensar em um número entre 0 e 5, tente adivinhar\033[m!')

print(linha3)
print(linha3_1)
print(frase3.center(70))
print(linha3_1)
print(linha3)
print(linha3_1)

escolha = int(input('\033[1;33m>>>\033[m Em que número eu pensei?\n\n\033[1;33m>>>\033[m Digite sua escolha: '))
print(linha3_1 * 3)

# RESULTADO

linhaf = ' ' * 60
frase_vitoria = ('O número {} foi exatamente o número que pensei, você acertou.'.format(escolha))
frase_vitoria1 = ('PARABÉNS!!!')

frase_final1 = '>>> FIM DE JOGO <<<'

frase_derrota = ('OPS! o número {} não foi o número que eu pensei. '.format(escolha))

frasecomplementar = ('Vamos lá, tente novamente...')

frase_final2 = ' \033[1;31m>>> FIM DE JOGO <<<\033[m '

if escolha == IA:

    print(linhaf * 2)
    print(frase_vitoria.center(60))
    print(linhaf)
    print(frase_vitoria1.center(60))
    print(linhaf * 3)
    print(frase_final1.center(60))

else:

    print(linhaf * 2)
    print(frase_derrota.center(60))
    print(frasecomplementar.center(60))
    print(linhaf * 3)
    print(frase_final2.center(69))



