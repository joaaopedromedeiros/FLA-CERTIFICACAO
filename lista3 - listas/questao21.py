valor = 0
contador = 0
valores = []
soma = 0
abaixo_media = []
acima_media = []

while contador < 5:
    novo = int(input("Digite um novo valor para média: "))
    contador += 1
    valores.append(novo)

for i in valores:
    soma += i
divisor = len(valores)

media = soma/divisor
for i in valores:
    if i < media:
        abaixo_media.append(i)
    elif i > media:
        acima_media.append(i)


    


#print(contador)
#print(valores)
#print(media)
print(f'Média: {media}')
print(f'Acima da média: {acima_media}')
print(f'Abaixo da média: {abaixo_media}')