tempoDeViagem = int(input())
velocidadeMedia = int(input())
distancia = tempoDeViagem*velocidadeMedia
gasto = distancia/12

print("{:.3f}".format(gasto))