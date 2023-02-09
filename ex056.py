print('\033[1:31mAPLICATIVO DE CADASTRAMENTO.\033[m')
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheres20 = 0
for programa in range(1, 5):
    print('*-'*15)
    nome = str(input('Nome: ')).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    mediaidade += idade / 4
    if programa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres20 += 1
print("A média de todas as idades é {:.1f}".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))
print("No total temos {} com menos de 20 anos.".format(mulheres20))








