lista = [3, 2, 6, 0]
a = 0

def logica(a, lista):
    soma = 0
    if a == 0:
        for i in lista:
            soma += i
    elif a > 0:
        for i in lista:
            if i % 2 == 0:
                soma += i
    elif a < 0:
        for i in lista:
            if i % 2 != 0:
                soma += i
    print(soma)
    return

logica(a,lista)


#retornar: a soma de todos os elementos da lista caso a = 0;
#a soma dos elementos pares da lista caso a > 0;
#a soma dos elementos ímpares da lista caso a < 0.
