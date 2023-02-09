print('='*25)
print("10 TERMOS DE UMA PA")
print('='*25)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + 1, razao):
    print('{}'.format(i), end=' > ')
print("Acabou.")


