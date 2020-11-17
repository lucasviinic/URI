tempo_str = input().split()

tempo_int = []
for i in tempo_str:
    tempo_int.append(int(i))

hi, mi = tempo_int[0], tempo_int[1]
hf, mf = tempo_int[2], tempo_int[3]

if hf == hi:
    tempo = (hf*60 + mf + 24*60) - (hi*60 + mi)
    horas = int(tempo/60)
    minutos = tempo - horas*60
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))
else:
    tempo = (hf*60 + mf) - (hi*60 + mi)
    horas = int(tempo/60)
    minutos = tempo - horas*60
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))
    



    