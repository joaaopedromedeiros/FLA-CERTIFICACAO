#Escreva um programa que define uma lista com elementos inteiros e que imprime os
#índices do menor elemento e do maior elemento da lista.


l = [3, 5, 6, 10, 7]
maior = 0
menor = 0

print(l.index(7))

for i in l:
    if i > maior:
        maior = i
        print(f'O maior elemento é {maior} e está no índice {l.index(maior)}')
    
    if i < menor:
        menor = i
        print(f'O menor elemento é {menor} e está no índice {l.index(menor)}')
    
    