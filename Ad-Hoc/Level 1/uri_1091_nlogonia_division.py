saida = []
while True:
    consul = int(input())
    if consul > 0:
        dp = [int(i) for i in input().split()]
        for j in range(consul):
            entrada = [int(i) for i in input().split()]
            if entrada[0] == dp[0] or entrada[1] == dp[1]:
                saida.append('divisa')
            elif entrada[0] > dp[0]:
                if entrada[1] > dp[1]:
                    saida.append('NE')
                else:
                    saida.append('SE')
            elif entrada[0] < dp[0]:
                if entrada[1] > dp[1]:
                    saida.append('NO')
                else:
                    saida.append('SO')
    else:
        for s in saida:
            print(s)
        break