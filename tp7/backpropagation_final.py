import numpy as np
import pandas as pd

data = pd.read_csv('/Users/maxiperellon/Desktop/Facultad/5quinto/Inteligencia Artificial/Tema 7 - Redes Neuronales/tp7/seeds_dataset.csv', sep=';')

X = np.array(data.iloc[0:len(data), 0:7])
y = np.array(data[['valor7']])

# X = X/np.amax(X, axis=0)
# y = y/100


class red_reuronal(object):
    def __init__(self):
        self.capa_entrada = 7
        self.capa_oculta = 1
        self.capa_salida = 3

        #pesos
        self.wi = np.random.randn(self.capa_entrada, self.capa_oculta)
        self.wj = np.random.randn(self.capa_oculta, self.capa_salida)
    
    def activacion(self, x):
        fx = 1/(1 + np.exp(-x))
        return fx

    def derivada(self, x):
        dx = x * (1 - x)
        return dx

    def propagacion_ad(self, X):
        self.z = np.dot(X, self.wi)
        self.zi = self.activacion(self.z)
        self.zj = np.dot(self.zi, self.wj)
        return self.activacion(self.zj)

    def propagacion_at(self, X, y, out):
        self.out_error = y - out
        self.out_d = self.out_error * self.derivada(out)
        self.zi_error = self.out_d.dot(self.wj.T)
        self.zi_d = self.zi_error * self.derivada(self.zi)

        #nuevos pesos
        self.wi += X.T.dot(self.zi_d)
        self.wj += self.zi.T.dot(self.out_d)

    def entrenar(self, X, y):
        pa = self.propagacion_ad(X)
        return self.propagacion_at(X, y, pa)

red = red_reuronal()

def entrenamiento():
    for i in range(1000):
        print('\n***************************************************************************')
        print('\n Entradas: \n\n', X)
        print('\n***************************************************************************')
        print('\nSalidas actuales: \n\n', y)
        print('\n***************************************************************************')
        # print('\nPredicción de salidas: \n\n', red.propagacion_ad(X))    
        print('\n[         1         ]' + '[         2         ]' + '[         3         ]')        
        print('\nPredicción de salidas: \n\n', [np.mean(red.propagacion_ad(X)[0])], [np.mean(red.propagacion_ad(X)[1])], [np.mean(red.propagacion_ad(X)[2])])
        print('\n***************************************************************************')
        print(np.mean(np.square(y - red.propagacion_ad(X))))
        red.entrenar(X, y)
    
entrenamiento()