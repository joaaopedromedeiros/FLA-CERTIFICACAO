#Escreva um programa que tem como saída a duração de uma corrida
#automobilística de longa duração que dura no máximo 24 horas. O programa tem 4
#entradas inteiras. As duas primeiras entradas correspondem à hora e aos minutos
#de início da corrida, enquanto que as duas últimas entradas correspondem à hora e
#aos minutos de término da corrida. Note que uma corrida pode iniciar em um dia e
#finalizar no dia seguinte.

horas = int(input("Informe a hora do inicio da corrida: "))
minutos = int(input("informe os minutos de incio da corrida"))
horas_t = int(input("Informe a hora de termino: "))
minutos_t = int(input("Informe os minutos de termino: "))


horasTotal = (horas * 60) + (horas_t * 60)
minutosIniciaisTotais = minutos +  minutos_t 
minutosCorrida = horasTotal + minutosIniciaisTotais





# converte tudo para minutos, depois converte


print(f"Duração da corrida foi: {minutosCorrida}h")