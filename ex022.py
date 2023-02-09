# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras sem espaços considerar ao t7do
# Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
mai = nome.upper()
print("Analisando seu nome...")
print('Seu nome em MAIÚSCULA: {}'.format(nome.upper()))
print("Seu nome em Minúsculas: {}".format(nome.lower()))
print("Seu nome em ao todo {} letras".format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))






