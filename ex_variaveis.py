nome = 'victor'
lista_valores = [1, 2, 10, 20, nome]
total = 0
for item in lista_valores:
    print(item)
    if item == nome:
        total = total
    else:
        total += item
    print(total)
