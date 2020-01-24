import random
import numpy as npy

def poblacion():
    poblacion = []
    for i in range(100):
        poblacion.append([])
        for j in range(4):
            poblacion[-1].append(random.randint(0,63))
    return poblacion

def elevacion(new_poblacion):
    elevacion = []
    for i in new_poblacion:
        A = i[0]
        B = i[1]
        C = i[2]
        D = i[3]
        elevacion.append((A - B)**2 + (C - D)**2 - (A -30)**3 - (C - 40)**3)
    return elevacion


# def probabilidad():
    

new_poblacion = poblacion()

# print(new_poblacion)
print(elevacion(new_poblacion))