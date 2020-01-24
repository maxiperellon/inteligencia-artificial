import random
import pandas as pd
import numpy as np

# Entradas y salidas
x0 = 1
x1 = [4.2,9.7,5.4,5.3]
x2 = [-1,-1,1,1]
x3 = [-1,-1,1,1]
x4 = [-1,-1,1,-1]
x5 = [-1,-1,1,-1]
y = [-1,1,1,-1]

iando = [x1,x2,x3,x4,x5,y]
datos = np.transpose(iando) 

# Pesos
w0 = -1
w1 = round(random.uniform(0, 1), 1)
w2 = round(random.uniform(0, 1), 1)
w3 = round(random.uniform(0, 1), 1)
w4 = round(random.uniform(0, 1), 1)
w5 = round(random.uniform(0, 1), 1)

# Taza de aprendizaje
r = 0.5

t_umbral = 0

def error_e(datos, n):
    error_e = datos[i][5] - n
    return error_e

def correccion(r, error_e):
    correccion_d = r * error_e
    return correccion_d

n0 = []

while n0 != y:
    print('x0', 'x1', ' x2', ' x3', ' x4', ' x5', ' y', ' w0', ' w1', ' w2', ' w3', ' w4', ' w5', ' s', ' n', ' e', ' d', ' nw0', ' nw1', ' nw2', ' nw3', ' nw4', ' nw5')
    n0 = []    
    for i in range(len(datos)):
        for j in range(0,4):
            suma_s = round(x0*w0 + datos[i][0]*w1 + datos[i][1]*w2 + datos[i][2]*w3 + datos[i][3]*w4 + datos[i][4]*w5)

        if (suma_s >= t_umbral):
            n = 1
            n0.append(n)
        else:
            n = -1
            n0.append(n)

        e = error_e(datos, n)
        cd = correccion(r, e)
       
        #nuevos pesos
        nw0 = round(w0 + x0*cd)
        nw1 = round(w1 + datos[i][0]*cd)
        nw2 = round(w2 + datos[i][1]*cd)
        nw3 = round(w3 + datos[i][2]*cd)
        nw4 = round(w4 + datos[i][3]*cd)
        nw5 = round(w5 + datos[i][4]*cd)


        print(x0, datos[i][0], datos[i][1], datos[i][2], datos[i][3], datos[i][4], datos[i][5], w0, w1, w2, w3, w4, w5, suma_s, '>', n, '<', e, cd, nw0, nw1, nw2, nw3, nw4, nw5)

        w0 = nw0
        w1 = nw1
        w2 = nw2
        w3 = nw3
        w4 = nw4
        w5 = nw5

    # break