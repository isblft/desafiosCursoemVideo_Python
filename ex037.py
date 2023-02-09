num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções:
(\033[34m 1 \033[m) Converter para BINÁRIO.
(\033[31m 2 \033[m) Converter para OCTAL.
(\033[35m 3 \033[m) Converter para HEXADECIMAL.''')
opção = int(input('\033[1m Opção escolhida: \033[m '))
if opção == 1:
    print('O número {} convertido para \033[1:34m BINÁRIO \033[m fica {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para \033[1:31m OCTAL \033[m fica {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para \033[1:35m HEXADECIMAL \033[m fica {}.'.format(num, hex(num)[2:]))
else:
    print('Opção \033[1:31m INVÁLIDA \033[m. Tente Novamente!')

#bin, oct, hex conversões e [2:] é o fatiamento da string
