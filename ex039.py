from datetime import date

genero = int(input('[1] \033[34mFeminino\033[m. [2] \033[31mMasculino\033[m.\nInforme o número correspondente ao seu '
                   'genêro: '))
if genero == 1:
    print('Você não precisa se alistar!')
elif genero == 2:
    atual = date.today().year
    nasc = int(input('Informe seu ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu no ano de {} tem {} em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alisar \033[1:33mIMEDIATAMENTE\033[m!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem idade para se alistar, faltam {} anos.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('\033[1:33m!!!!Opção não reconhecida!!!!\033[m')
