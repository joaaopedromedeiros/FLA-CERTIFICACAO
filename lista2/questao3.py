x = int(input("Valor: "))

soma = 0

for i in range(1,x+1):
    if i % 2 == 0:
        atual = i
        soma = atual + soma

print(soma)
