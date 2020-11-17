while True:
    try:
        N, M = [int(i) for i in input().split()]
        if N == M == 0:
            break

        T = [int(j) for j in input().split()]
        falsos = 0 
        for k in range(1,N+1):
            if T.count(k) > 1:
                falsos += 1
        
        print(falsos)
    except EOFError:
        break

