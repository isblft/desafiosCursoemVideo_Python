print('\033[1:31mCALCULADORA DE DESCONTOS DA ISABELA!\033[m')
valor = float(input('Digite o valor total: R$'))
pagamento = int(input('''(1) A VISTA(DINHEIRO OU CHEQUE).\n(2) Á VISTA NO CARTÃO.\n(3) PARCELADO ATÉ 2X NO CARTÃO.\n(4) PARCELADO ATÉ 3X NO CARTÃO.
Digite o número referente a forma de pagamento desejada: '''))
if pagamento == 1:
    desconto = valor - (10/100 * valor)
    print('O valor de R${:.2f} no pagamento a vista.\nRecebe um desconto de 10%, ficando então R${:.2f}.'.format(valor, desconto))
elif pagamento == 2:
    desconto2 = valor - (5/100 * valor)
    print("O valor de R${:.2f} no pagamento á vista no Cartão.\nRecebe um desconto de 5%, totalizando R${:.2f}!".format(valor, desconto2))
elif pagamento == 3:
    preçof = valor / 2
    print("O valor de R${:.2f} em 2x totaliza duas parcelas de R${:.2f}".format(valor, preçof))
elif pagamento ==4:
    parcelas = int(input("Quantas parcelas?"))
    total = valor+(20/100*valor)
    t = total / parcelas
    print('O valor de R${:.2f} no pagamento até 3x ou mais no Cartão recebe um acréscimo de 20%, ficando R${:.2f}. Totalizando '
          '{} parcelas, no valor de R${:.2f}.'.format(valor, total, parcelas, t))
else:
    print('FORMA DE PAGAMENTO NÃO RECONHECIDA. TENTE NOVAMENTE!')







