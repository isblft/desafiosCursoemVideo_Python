#Escreva um programa que faça o computador “pensar” em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
from random import randint
from time import sleep

pronto = str(input('Você está pronto para jogar? (Sim/Não)')).lower()
if pronto == "sim":
    print('Vamos brincar de adivinhar?? \nPensarei em um número de 0 a 5, e você terá que adivinhar!')
    nc = randint(0, 5) # faz o computador pensar
    nu = int(input('Em que número eu pensei?? ')) #usuario tenta adivinhar
    print('PROCESSANDO...')
    sleep(2)
    if nu == nc:
        print('Você acertou!! Parábens!!!')
    else:
        print('Você perdeu!!! :p Eu pensei no número {} e não no {}.'.format(nc, nu))
elif pronto == "não":
    print('Que pena!')


