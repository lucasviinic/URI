ladosStr = input().split()
A, B, C = float(ladosStr[0]), float(ladosStr[1]), float(ladosStr[2])

if (B + C > A) and (A + C > B) and (A + B > C):
    perimetro = A + B + C
    print("Perimetro = {}".format(perimetro))
else:
    area = ((A + B) * C)/2
    print("Area = {}".format(area))
