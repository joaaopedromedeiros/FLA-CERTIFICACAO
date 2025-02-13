a = [5, -2, 3]

def par_impar_soma(a):
    par = 0
    impar = 0
    for i in a:
        if i % 2 == 0:
            par += i
        if i % 2 != 0:
            impar += i
    print(f'Par: {par} Impar: {impar}')
    return par, impar

par_impar_soma(a)
