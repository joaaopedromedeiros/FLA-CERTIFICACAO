
lista1 = [3, 2, 6, 0]
lista2 = [0, 5, 2]

def Juntar_Sem_Repertir(a,b):
    uniao = []
    for i in a:
        uniao.append(i)
    for i in b:
        uniao.append(i)
    print(uniao)

    lista = []
    for i in uniao:
        if i not in lista: #faltou usar not in, in ....... faltou isso
            lista.append(i)
    print(lista)
        

Juntar_Sem_Repertir(lista1,lista2)




        


