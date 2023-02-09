#004 FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSIVEIS.
var1 = (input('Digite algo: '))
print('O tipo primitivo desse valor é ', type(var1))
print('Só tem números? ', var1.isnumeric())
print(var1.isalpha())
print(var1.isalnum())
print(var1.islower())
print(var1.isupper())
print(var1.isdecimal())
print(var1.isdigit())
print(var1.isascii())
print(var1.isprintable())
print('É um titulo? ', var1.istitle())
print('Só tem espaços? ', var1.isspace())



