print('Me diga o valor de 3 retas e eu lhe direi se é possivel ou não formar um triângulo...')
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim, é possivel formar um triângulo!')
else:
    print('No no, não é possivel formar um triângulo!')

