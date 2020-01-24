import random
import numpy as np

def individuo():
    cartas=list(range(1,11))
    random.shuffle(cartas)
    return cartas

def poblacion():
    poblacion = []
    for i in range(100):
        poblacion.append(individuo())
    return poblacion

new_poblacion = poblacion()

def suma_and_mult():
    sumas = []
    mult = []
    for i in range(len(new_poblacion)):
        suma = sum(new_poblacion[i][:5])
        sumas.append(suma)
        m = np.prod(new_poblacion[i][5:10])
        mult.append(m)
    return sumas, mult
    
# print(suma_and_mult())

def funcion_adaptacion_seleccion():
    cont = 0
    individuos = []
    for i in range(len(new_poblacion)):
        for j in range(5):
            if  suma_and_mult()[0][i]/36 == 1 and suma_and_mult()[1][i]/360 == 1:
                cont += 1
                individuos.append(new_poblacion[i])
    return cont, individuos

# print('Cantidad de valores que la suma se aproxima a 36 y la multiplicación a 360 : ', funcion_adaptacion_seleccion())

def cruza():
