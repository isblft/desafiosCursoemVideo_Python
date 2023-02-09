salario = float(input('Qual o valor do seu salário?'))
if salario >= 1250:
    ssuperior = salario + (10/100*salario)
    print('O valor do salário aumentado é de {:.2f}'.format(ssuperior))
else:
    sinferior = salario + (15/100*salario)
    print('O valor do salário aumentado é de {:.2f}'.format(sinferior))
