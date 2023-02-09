import time
from random import randint
print('\033[1:35mVAMOS JOGAR JOKENPÔ?!\033[m')
jogador = int(input('''<0> PEDRA\n<1> PAPEL\n<2> TESOURA\nHumano, faça sua jogada: '''))
lista = ['PEDRA', 'PAPEL', 'TESOURA']
pc = randint(0, 2)
time.sleep(1)
print('\033[1:35mJO')
time.sleep(1)
print('\033[1:35mKEN')
time.sleep(1)
print('PÔ\033[m')
print('-*' * 15)
print('Sua jogada foi: {}!\nMinha jogada: {}!'.format(lista[jogador], lista[pc]))
print('-*' * 15)
time.sleep(1)
if pc == 0:
    if jogador == 0: #pedra
        print("\033[1:33mEMPATAMOS!\033[m")
    elif jogador == 1: #papel
        print("\033[4:32mVOCÊ VENCEU!. PAPEL EMBRULHA PEDRA!\033[m")
    elif jogador == 2: #tesoura
        print("\033[1:31mVOCÊ PERDEU! PEDRA QUEBRA TESOURA!\033[m")
    else:
        print('\033[1:33mJOGADA INVÁLIDA!\033[m')
elif pc == 1: #papel
    if jogador == 0: #pedra
        print('\033[1:31mVOCÊ PERDEU. PAPEL EMBRULHA PEDRA!\033[m')
    elif jogador == 1:
        print('\033[1:33mEMPATAMOS\033[m')
    elif jogador == 2: #tesoura
        print("\033[4:32mVOCÊ VENCEU. TESOURA CORTA PAPEL!\033[m")
    else:
        print("\033[1:31mJOGADA INVÁLIDA!\033[m")
elif pc == 2:
    if jogador == 0:
        print("\033[1:32mVOCÊ VENCEU. PEDRA QUEBRA TESOURA!\033[m")
    elif jogador == 1:
        print("\033[1:31mVOCÊ PERDEU. TESOURA CORTA PAPEL!\033[m")
    elif jogador == 2:
        print("\033[1:33mEMPATAMOS\033[m")
    else:
        print('\033[1:31m JOGADA INVÁLIDA\033[m')
