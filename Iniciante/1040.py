numbsS = input().split()
numbsF = []

for n in numbsS:
    numbsF.append(round(float(n), 1))
media = (2*numbsF[0] + 3*numbsF[1] + 4*numbsF[2] + numbsF[3])/10

print("Media: {:.1f}".format(media))
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
elif 5 <= media <= 6.9:
    print("Aluno em exame.")

    notaExame = float(input())
    print("Nota do exame: {:.1f}".format(notaExame))
    mediaFinal = (media + notaExame)/2

    if mediaFinal >= 5:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(mediaFinal))
    else:
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(mediaFinal))



