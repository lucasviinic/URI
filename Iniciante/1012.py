#Área
#entrada = ['A', 'B', 'C']
entrada = input().split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

areaTriangulo = (A * C)/2
areaCirculo = 3.14159 * C**2
areaTrapezio = ((A + B)*C)/2
areaQuadrado = B**2
areaRetangulo = A * B

print("TRIANGULO: {:.3f}".format(areaTriangulo))
print("CIRCULO: {:.3f}".format(areaCirculo))
print("TRAPEZIO: {:.3f}".format(areaTrapezio))
print("QUADRADO: {:.3f}".format(areaQuadrado))
print("RETANGULO: {:.3f}".format(areaRetangulo))