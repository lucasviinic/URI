n = int(input())
frequencia = {}

def conta_frequencia(valor):
    if valor in frequencia:
        frequencia[valor] += 1
    else:
        frequencia[valor] = 1

def ordena_invertido(dicionario):
    dic_key = []

    for i in dicionario:
        dic_key.append(i)
    dic_key = sorted(dic_key)
    
    for j in dic_key:
        print("{} aparece {} vez(es)".format(j, dicionario[j]))
i = 1
while i <= n:
    x = int(input())
    conta_frequencia(x)
    i += 1

ordena_invertido(frequencia)