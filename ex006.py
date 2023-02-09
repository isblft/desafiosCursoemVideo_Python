#CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO,TRIPLO E RAIZ QUADRADADA.
n = int(input('Digite um número: '))
d = n *2
d3 = n *3
rq = n **(1/2)
# Fazendo tudo direto
# print('O número é {}, O dobro dele é {} O triplo dele é {} e sua raiz é {}'. format(n, (n*2), (d*3),(n**(1/2)))
print('O número é {}, o dobro dele é {}.\nO triplo dele é {}. \nE sua raiz é {:.2}'. format(n, d, d3, rq))

#fazendo raiz de outro jeito pow(n. (1/2)
print('Olha só, mais um concluído hehe, siga asssim!!!')