#Escreve um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
m = float(input('Insira uma distância em Metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000


print('{:.1f} metros, equivalem a:\n{}km\n{}hm\n{:}dam\n{:.1f}dm\n{:.1f}cm.\n{:.1f}mm.'. format(m, km, hm, dam, dm, cm, mm))

#correção guanabara
#
#
#
#
#
#
#
#
#
#
#
#
#
#
