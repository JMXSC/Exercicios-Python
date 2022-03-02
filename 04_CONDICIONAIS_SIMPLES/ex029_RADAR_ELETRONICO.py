# Exercício Python 29: Escreva um programa que:
# a) leia a velocidade de um carro.
# B) Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# OBS: A multa vai custar R$7,00 por cada Km acima do limite.

linha = ' ' * 60

velocidade = float(input('Digite a velocidade em que o motorista estava digindo: '))

print(linha)

velocidade_permitida = 80
valor_multa = (velocidade - 80) * 7

if velocidade > 80:

    linhai = ' ' * 60

    print('Você foi MULTADO por estar dirigindo a {} KM/h numa pista de {} KM/h.'.format(velocidade,
                                                                                         velocidade_permitida))

    print(linhai)

    print('Sua multa irá custar R$ {:.2f}.'.format(valor_multa))

else:

    linhae = ' ' * 60
    frase = ('Tenha um bom dia! Dirija com segurança.')
    print(frase.center(60))
