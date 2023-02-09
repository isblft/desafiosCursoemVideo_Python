med1 = float(input("Primeira medida: "))
med2 = float(input("Segunda medida: "))
med3 = float(input("Terceira medida:"))
if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med2 + med1:
    print("As medidas acima PODEM FORMAR um triângulo: ", end='')
    if med1 == med2 == med3:
        print("\033[1mEQUILÁTERO\033[m")
    if med1 != med2 != med3 != med1:
        print('\033[1mESCALENO!\033[m')
    else:
        print("\033[1mISÓSCELES!\033[m")
else:
    print('\033[31mNão é possivel formar um triângulo.\033[m')

# escalono lados diferentes
#equilateres lados iguais
#ISOSCELES QND DUAS SÃO IGUAIS

