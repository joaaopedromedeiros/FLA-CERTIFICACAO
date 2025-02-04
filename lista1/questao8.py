caixa = float(input("Digite o valor: "))

bolo = 8.50

bolos = caixa // bolo
troco = caixa - (bolos * bolo)
print(f'Bolos: {bolos}')


if troco == 0:
    print("Sem troco")
else:
    print(f'Troco: {troco}') 