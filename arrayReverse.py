def reverse(lista):
    nlista = []
    while len(lista) > 0:
        nlista.append(lista[-1])
        del(lista[-1])
    print(nlista)

reverse([0,1,2,3,4,5])