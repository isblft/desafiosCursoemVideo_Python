n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2)/2
print('Sua média é {:.1f}'.format(media))
if media < 5.0:
    print('\033[1:31mREPROVADO!\033[m')
elif media > 7.0:
    print('\033[1:32mAPROVADO!\033[m')
else:
    print('\033[1:33mRECUPERAÇÃO!\033[m')

    # a idade é maior igual a 10, só que a média é menor que 14
    # outra opção idade >=10 and idade < 14:




