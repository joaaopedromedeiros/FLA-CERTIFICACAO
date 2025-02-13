a = []
print(len(a))
def media_lista(lista):
    somatotal = 0
    divisor = len(lista)

    for i in lista:
        somatotal += i
    try:
        media = somatotal / divisor
        print(f'A média aritimédica simples é: {media}')
        return media
    except ZeroDivisionError:
        return None

media_lista(a)
