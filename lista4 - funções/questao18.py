lista1 = [3, 2, 6, 0]

def pares_impares(a):
    pares = []
    impares = []
    for i in a:
        if i % 2 == 0:
            pares.append(i)
        elif i % 2 != 0:
            impares.append(i)
    print(pares)
    print(impares)
    return pares, impares

pares_impares(lista1)