verificador = 1
pares = []
impares = []

while verificador > 0:
    numero = int(input("Digite um novo valor para verificar se é impar ou par: "))
    verificador = numero
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    print(f'Pares: {pares}')
    print(f'Impares: {impares}')
