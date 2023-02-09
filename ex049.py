n = int(input("Digite um número: "))
print('\033[33m-*\033[m'*40)
for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, n*c))
