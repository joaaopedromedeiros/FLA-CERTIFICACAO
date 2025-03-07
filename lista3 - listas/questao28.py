l = [3,2,9,7,9]
l1 = [3,8,4,6,9]
repetidos = []
interssesao = []



for i in l:
    if i in l1:
        repetidos.append(i)

for i in repetidos:
    if i in interssesao:
        continue
    interssesao.append(i)

print(repetidos)
print(interssesao)

