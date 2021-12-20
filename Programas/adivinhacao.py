import random as rd
from random import randrange

def saudacoes():
    print('\n ______________________________________________________________________________')
    print('|Tenho um número entre 0 e 100 escondido aqui, boa sorte para tentar adivinhar!|')
    print(' ______________________________________________________________________________\n')

def verificaNumero(tentativa, numero):
    if numero == tentativa:
        return True
    return False

def verificaJogarNovamente(resposta):
    if resposta == 's':
        return True
    return False

def dica(tentativa, numero):
    if tentativa < numero:
        print('O número é maior que ' + str(tentativa))
    else:
        print('O número é menor que ' + str(tentativa))
    
saudacoes()
jogador1 = input('Nome do Jogador 1: ')
jogador2 = input('Nome do Jogador 2: ')

nSecreto = rd.randrange(99,100)

while True:
    tentativa = int(input('Tente a sorte '+ jogador1 + ': '))
    if verificaNumero(tentativa, nSecreto):
        print('Mandou bem ' + jogador1 + '!!!')
        jogarNovamente = input('Jogar novamente? (s/n): ')
        if verificaJogarNovamente(jogarNovamente):
            nSecreto = rd.randrange(100)
            saudacoes()
            continue
        break
    dica(tentativa, nSecreto)
    
    tentativa = int(input('Tente a sorte '+ jogador2 + ': '))
    if verificaNumero(tentativa, nSecreto):
        print('Mandou bem ' + jogador2 + '!!!')
        jogarNovamente = input('Jogar novamente? (s/n): ')
        if verificaJogarNovamente(jogarNovamente):
            nSecreto = rd.randrange(100)
            saudacoes()
            continue
        break
    dica(tentativa, nSecreto)