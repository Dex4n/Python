contFaltanteFrango = 0
contFaltanteBife = 0
contFaltanteMassa = 0
totalFaltante = 0

line1 = input().split()

frangoTotal = int(line1[0])
bifeTotal = int(line1[1])
massaTotal = int(line1[2])

line2 = input().split()

pedidoFrango = int(line2[0])
pedidoBife = int(line2[1])
pedidoMassa = int(line2[2])


if pedidoFrango > frangoTotal:
    contFaltanteFrango = pedidoFrango - frangoTotal
    totalFaltante += contFaltanteFrango
if pedidoBife > bifeTotal:
    contFaltanteBife = pedidoBife - bifeTotal
    totalFaltante += contFaltanteFrango
if pedidoMassa > massaTotal:
    contFaltanteMassa = pedidoMassa - massaTotal
    totalFaltante += contFaltanteFrango





totalFaltante = contFaltanteFrango + contFaltanteBife + contFaltanteMassa

print(totalFaltante)
