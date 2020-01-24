#Casado - Fiochetti - Perellón

# hipotesis más especifica
h = ['0', '0', '0', '0', '0']

# hipotesis general

g = ['?', '?', '?', '?', '?']

entrenamiento = [
     ['sunny', 'hot', 'high', 'weak', 'False'],
     ['sunny', 'hot', 'high', 'strong', 'False'],
     ['overcast', 'hot', 'high', 'weak', 'True'],
     ['rain', 'mild', 'high', 'weak', 'True'],
     ['rain', 'cool', 'normal', 'weak', 'True'],
     ['rain', 'cool', 'normal', 'strong', 'False'],
     ['overcast', 'cool', 'normal', 'strong', 'True'],
     ['sunny', 'mild', 'high', 'weak', 'False'],
     ['sunny', 'cool', 'normal', 'weak', 'True'],
     ['rain', 'mild', 'normal', 'weak', 'True'],
     ['sunny', 'mild', 'normal', 'strong', 'True'],
     ['overcast', 'mild', 'high', 'strong', 'True'],
     ['overcast', 'hot', 'normal', 'weak', 'True'],
     ['rain', 'mild', 'high', 'strong', 'False']
]


def true_values():

    entrenamiento.remove(entrenamiento[0])
    entrenamiento.remove(entrenamiento[0])
    entrenamiento.remove(entrenamiento[3])
    entrenamiento.remove(entrenamiento[4])
    entrenamiento.remove(entrenamiento[9])
    # print(entrenamiento)
    return entrenamiento


def found_E():
    entrenamiento = true_values()
    entrenamiento_1 = len(entrenamiento)
    found_array_E = []
    true_array = []
    found_array_E.append(h)
    for i in range(0, entrenamiento_1):
        for j in range(0, 5):
            if i == 0:
                if entrenamiento[i][j] == entrenamiento[0][j]:
                    found_array_E.append(entrenamiento[i][j])
                else:
                    found_array_E.append(g[0][0])

            elif i >= 1:
                if entrenamiento[i][j] == entrenamiento[i - 1][j]:
                    found_array_E.append(entrenamiento[i][j])
                else:
                    found_array_E.append(g[0][0])
    true_array.append(found_array_E[:6])
    true_array.append(found_array_E[6:11])
    true_array.append(found_array_E[11:16])
    true_array.append(found_array_E[16:21])
    true_array.append(found_array_E[21:26])
    true_array.append(found_array_E[26:31])
    true_array.append(found_array_E[31:36])
    true_array.append(found_array_E[36:41])
    true_array.append(found_array_E[41:46])
    # print(true_array)
    return true_array


def transform():
    true_array = found_E()
    true_array_1 = len(true_array)
    for i in range(1, true_array_1):
        for j in range(0, 4):
            if true_array[i - 1][j] == g[0][0]:
                true_array[i][j] = g[0][0]
    print(true_array)


transform()
