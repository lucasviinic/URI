N = int(input())

if 0 < N < 1000000:
    notas100 = int(N/100)
    notas50 = int((N % 100)/50)
    notas20 = int(((N % 100) % 50)/20)
    notas10 = int((((N % 100) % 50)%20)/10)
    notas5 = int(((((N % 100) % 50)%20)%10)/5)
    notas2 = int((((((N % 100) % 50)%20)%10)%5)/2)
    notas1 = int((((((N % 100) % 50)%20)%10)%5)%2)

    print(N)
    print("{} nota(s) de R$ 100,00".format(notas100))
    print("{} nota(s) de R$ 50,00".format(notas50))
    print("{} nota(s) de R$ 20,00".format(notas20))
    print("{} nota(s) de R$ 10,00".format(notas10))
    print("{} nota(s) de R$ 5,00".format(notas5))
    print("{} nota(s) de R$ 2,00".format(notas2))
    print("{} nota(s) de R$ 1,00".format(notas1))

