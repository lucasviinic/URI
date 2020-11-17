#N ---> Numero de perguntas realizadas
#K ---> Numero de vezes que uma pergnta deve ser feita para ser considerada "frequente"
while True:
    N, K = [int(i) for i in input().split()]
    if N == K == 0:
        break

    P = [int(j) for j in input().split()]
    perguntas_frequentes = 0

    for l in range(1, 101):
        if P.count(l) >= K:
            perguntas_frequentes += 1
    
    print(perguntas_frequentes)
