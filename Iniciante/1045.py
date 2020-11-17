lados_str = input().split()

lados_num = []
for n in lados_str:
    lados_num.append(float(n))
lados_num = sorted(lados_num, reverse=True)

a, b, c = lados_num[0], lados_num[1], lados_num[2]

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    if a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    if a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
    if a == (b and c):
        print("TRIANGULO EQUILATERO")
    if ((a == b) and c != (a and b)) or ((b == c) and a != (b and c)) or ((c == a) and b != (c and a)):
        print("TRIANGULO ISOSCELES")

