#entrada = ['A', 'B', 'C', 'D']
entrada = input().split()
A = int(entrada[0])
B = int(entrada[1])
C = int(entrada[2])
D = int(entrada[3])

if (B > C) and (D > A) and ((C + D) > (A + B)) and ((C and D) >= 0) and ((A % 2) == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")