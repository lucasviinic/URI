def tautograma(texto):
    frase = texto.lower().split()
    char_reference = frase[0][0]
    is_tautograma = True

    if frase[0] != "*":
        for word in frase:
            if word[0] != char_reference:
                is_tautograma = False
        if is_tautograma == True:
            print("Y")
        else:
            print("N")
    else:
        pass

while True:
    entrada = input()
    if entrada != "*":
        tautograma(entrada)
    else:
        break
