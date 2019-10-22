line1 = input().split()
cod1 = int(line1[0])
nump1 = float(line1[1])
valor1 = float(line1[2])

line2 = input().split()
cod2 = int(line2[0])
nump2 = float(line2[1])
valor2 = float(line2[2])


xt = (nump1 * valor1) + (nump2 * valor2)


print('VALOR A PAGAR: R$','{:.2f}'.format(xt))