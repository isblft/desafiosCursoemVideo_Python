casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual valor do salário: R$ '))
anos = int(input("Em quantos anos planeja pagar? "))
pm = casa / (anos * 12)
#ps = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação mensal será de R${:.2f}'.format(casa, anos, pm))
if pm <= 30/100 * salario:
 print("Empréstimo Aceito. Parabens!!")
else:
    print('Empréstimo \033[1:31m Negado\033[m!')
