values_str = input().split()
x = round(float(values_str[0]), 1)
y = round(float(values_str[1]), 1)

if x == 0 and y == 0:
    print("Origem")
elif (y == 0) and (x != 0):
    print("Eixo X")
elif (x == 0) and (y != 0):
    print("Eixo Y")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
