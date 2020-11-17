from math import sqrt

coeficientes = input().split()
A = float(coeficientes[0])
B = float(coeficientes[1])
C = float(coeficientes[2])

delta = (B**2) + (-4 * A * C)

if (delta >= 0) and (A != 0) :
    r1 = (-1*B + sqrt(delta))/(2*A)
    r2 = (-1*B - sqrt(delta))/(2*A)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))
else:
    print("Impossivel calcular")
