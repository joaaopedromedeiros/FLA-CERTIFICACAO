
lista1 = [1,2,3]
lista2 = [4,5,6]

def juntar(a,b):
    listanova = []
    for i in a:
        listanova.append(i)
    
    for i in b:
        listanova.append(i)
    print(listanova)
    return listanova

juntar(lista1,lista2)
j