num1 = int(input("\033[1mPrimeiro valor: "))
num2 = int(input("\033[1mSegundo valor: "))
escolha = 0
while escolha != 5:
    print('*+'*30)
    print('''\033[1m[1]Somar.\n[2]Multiplicar.\n[3]Maior.\n[4]Digitar novos números.\n[5]Sair do Programa.''')
    escolha = int(input(">>> Digite o número referente ao que deseja: "))
    if escolha == 1:
        print(">>> Você escolheu somar os números!")
        r = num2+num1
        print(">>> {} + {} = {}. ".format(num2, num1, r))
    elif escolha == 2:
        print(">>> Você escolheu Multiplicar os valores!")
        r = num2*num1
        print('>>> {} x {} = {}.'.format(num2, num1, r))
    elif escolha == 3:
        print('>>> Você quer saber qual valor é maior!')
        if num1 > num2:
            maior = num1
        else:
            maior = num2
            print('>>> Entre {} e {}, o maior valor é {}'.format(num1, num2, maior))
    elif escolha == 4:
        print('>>> Você escolheu digitar novos números <<<!')
        print("Informe os números novamente: ")
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundoo valor: "))
    elif escolha == 5:
        print('Finalizando..')
print("Fim do Programa. Volte sempre!")

