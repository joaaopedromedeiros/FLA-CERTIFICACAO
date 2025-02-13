
lista1 = [0, 2, 4]
lista2 = [1, 3]

def intersessao(a,b):
    listanova = []

    for i in (a and b):
        if i in a and i in b: # pode fazer assim, i in b, i in a, etccc. 
           listanova.append(i)
    print(listanova)

intersessao(lista1,lista2)
