N = int(input())
horas = int(N/3600)
minutos = 60 * (N/3600 - horas)
segundos = 60 * (minutos - int(minutos))

print("{}:{}:{}".format(horas, int(round(minutos, 2)), int(round(segundos, 2))))

