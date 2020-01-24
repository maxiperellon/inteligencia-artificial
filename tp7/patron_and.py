import random
import pandas as pd
import numpy as np

# Entradas y salidas
x0 = 1
x1 = [0,0,1,1]
x2 = [0,1,0,1]
y = [0,0,0,1]

iando = [x1,x2,y]
datos = np.transpose(iando) 

# Pesos
w0 = -1
w1 = round(random.uniform(0, 1), 1)
w2 = round(random.uniform(0, 1), 1)

#taza de aprendizaje
r = 0.2

cont_error = 0
t_umbral = 0

def error_e(datos, n):
    error_e = datos[i][2] - n
    return error_e

def correccion(r, error_e):
    correccion_d = r * error_e
    return correccion_d

while cont_error != 4:
    print('x0', 'x1', 'x2', 'y', 'w0', 'w1', 'w2', 's', 'n', 'e', 'd', 'nw0', 'nw1', 'nw2')
    for i in range(len(datos)):
        for j in range(0,2):
            suma_s = x0*w0 + datos[i][0]*w1 + datos[i][1]*w2
            suma_s = round(suma_s,2)

            if (suma_s >= t_umbral):
                n = 1
            else:
                n = 0

        e = error_e(datos, n)
        cd = correccion(r, e)

        cont_error += 1
       
        #nuevos pesos
        nw0 = w0 + x0*cd
        nw1 = w1 + datos[i][0]*cd
        nw2 = w2 + datos[i][1]*cd

        print(x0, datos[i][0], datos[i][1], datos[i][2], w0, w1, w2, suma_s, n, e, cd, nw0, nw1, nw2)

        w0 = nw0
        w1 = nw1
        w2 = nw2


