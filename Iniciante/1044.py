values = input().split()
A, B = int(values[0]), int(values[1])

if (B % A == 0) or (A % B == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")