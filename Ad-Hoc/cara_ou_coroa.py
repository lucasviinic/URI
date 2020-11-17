while True:
    N = int(input())
    if N == 0:
        break
    Ri = [int(i) for i in input().split()]
    Mary = Ri.count(0)
    John = Ri.count(1)
    print("Mary won {} times and John won {} times".format(Mary, John))