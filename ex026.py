#26 Faça um programa que leia uma frase pelo teclado e mostre quantas
# vezes aparece a letra “A”, em que posição ela aparece a primeira vez e
# em que posição ela aparece a última vez.
frase = str(input('Escreva uma frase: ')).upper().strip()
print('Analisando a frase...')
print('Na sua frase, a letra A, aparece {} vezes.'.format(frase.count("A")))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {} '.format(frase.rfind('A')+1))

#divida o programa em pedações
#sempre pense ocmo usuário
