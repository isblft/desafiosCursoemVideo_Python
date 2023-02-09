import time
from random import randint
#from time import sleep
print("\033[1:32m!!VAMOS BRINCAR DE ADIVINHAR!!\033[m\n\033[1mVou pensar em um número de 0 a 10"
      " e você terá que adivinhar!\033[m")
numcomputador = randint(0, 10)
tentativas = 0
ganhei = False
while not ganhei:
    nummusuario = int(input("Qual se palpite? "))
    time.sleep(2)
    tentativas = tentativas + 1
    if nummusuario == numcomputador:
        ganhei = True
    else:
        if nummusuario < numcomputador:
            print('Mais... Tente novamente!')
        elif nummusuario > numcomputador:
            print("Menos... Tente novamente!")
print("\033[1:32mVocê acertou!\033[m\nE tentou {} vezes, antes de me vencer!\n\033[1:33mParabéns!!\033[m".format(tentativas))








