#O Maior
valores = input().split()
valoresNum = []
for n in valores:
    valoresNum.append(int(n))

print("{} eh o maior".format(max(valoresNum)))