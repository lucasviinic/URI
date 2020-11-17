pedido = input().split()

table = [[1, "Cachorro Quente", 4],
        [2, "X-Salada", 4.5],
        [3, "X-Bacon", 5],
        [4, "Torrada simples", 2],
        [5, "Refrigerante", 1.5]]

total = table[int(pedido[0])-1][2] * int(pedido[1])
print("Total: R$ {:.2f}".format(total))