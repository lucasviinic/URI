valueStr = input().split()

valueNum = []
for n in valueStr:
    valueNum.append(int(n))
valueNum = sorted(valueNum)

for i in valueNum:
    print(i)
print("")
for i in valueStr:
    print(i)

#sorted() <- Ordena os valores da lista em ordem crescente