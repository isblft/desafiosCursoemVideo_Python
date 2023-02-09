print('\033[1:35:46m Vamos comparar números!\033[m')
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
if n1 > n2:
    print('O \033[1:34mPRIMEIRO\033[m número é maior!')
elif n1 < n2:
    print('O \033[1:36mSEGUNDO\033[m número é maior!')
elif n1 == n2:
    print('\033[1:31m Não existe número maior ou menor. Os dois são iguais!\033[m')

#como não existe uma quarta opção poderia- se escrever apos o segundo elif
#else:
#    print('Os dois são iguais')
