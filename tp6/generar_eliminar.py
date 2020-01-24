#Casado - Fiochetti - Perellón

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

# hipotesis más especifica
h = ['0', '0', '0', '0', '0']

# hipotesis general
g = ['?', '?', '?', '?', '?']


def value_true():
    entrenamiento_1 = len(entrenamiento)
    true_array = []
    new_true_array = []
    for i in range(0, entrenamiento_1):
        for j in range(0, 5):
            if entrenamiento[i][4] == 'True':
                true_array.append(entrenamiento[i][j])
    
    new_true_array.append(true_array[:5])
    new_true_array.append(true_array[5:10])
    new_true_array.append(true_array[10:15])
    new_true_array.append(true_array[15:20])
    new_true_array.append(true_array[20:25])
    new_true_array.append(true_array[25:30])
    new_true_array.append(true_array[30:35])
    new_true_array.append(true_array[35:40])
    new_true_array.append(true_array[40:45])
    
    return new_true_array

print('\n')
print('Valores positivos:' + '\n' + '\n', value_true())
print('\n')


def value_false():
    entrenamiento_1 = len(entrenamiento)
    false_array = []
    new_false_array = []
    for i in range(0, entrenamiento_1):
        for j in range(0, 5):
            if entrenamiento[i][4] == 'False':
                false_array.append(entrenamiento[i][j])

    new_false_array.append(false_array[:5])
    new_false_array.append(false_array[5:10])
    new_false_array.append(false_array[10:15])
    new_false_array.append(false_array[15:20])
    new_false_array.append(false_array[20:25])

    return new_false_array

print('Valores negativos:' + '\n' + '\n', value_false())
print('\n')


def especifica():
    entrenamiento = value_true()
    entrenamiento_1 = len(entrenamiento)
    found_array = []
    true_array = []
    for i in range(0, entrenamiento_1):
        for j in range(0, 5):
            if i == 0:
                if entrenamiento[i][j] == entrenamiento[0][j]:
                    found_array.append(entrenamiento[i][j])
                else:
                    found_array.append(g[0][0])

            elif i >= 1:
                if entrenamiento[i][j] == entrenamiento[i - 1][j]:
                    found_array.append(entrenamiento[i][j])
                else:
                    found_array.append(g[0][0])

    true_array.append(h)
    true_array.append(found_array[:5])
    true_array.append(found_array[5:10])
    true_array.append(found_array[10:15])
    true_array.append(found_array[15:20])
    true_array.append(found_array[20:25])
    true_array.append(found_array[25:30])
    true_array.append(found_array[30:35])
    true_array.append(found_array[35:40])
    true_array.append(found_array[40:45])


    print('****************Frontera más específica*****************' + '\n')
    return true_array


def transform_especifica():
    true_array = especifica()
    true_array_1 = len(true_array)
    for i in range(1, true_array_1):
        for j in range(0, 4):
            if true_array[i - 1][j] == g[0][0]:
                true_array[i][j] = g[0][0]
    print(true_array)


def general():
    entrenamiento = value_false()
    entrenamiento_1 = len(entrenamiento)
    found_array = []
    false_array = []
    for i in range(0, entrenamiento_1):
        for j in range(0, 5):
            if i == 0:
                if entrenamiento[i][j] == 'sunny':
                        found_array.append(['overcast', '?', '?', '?'])
                        found_array.append(['rain', '?', '?', '?'])
                if entrenamiento[i][j] == 'hot':
                        found_array.append(['?', 'mild', '?', '?'])
                        found_array.append(['?', 'cool', '?', '?'])
                if entrenamiento[i][j] == 'high':
                        found_array.append(['?', '?', 'normal', '?'])
                if entrenamiento[i][j] == 'weak':
                        found_array.append(['?', '?', '?', 'strong'])
            
            if i >= 1:
                if entrenamiento[i][j] == 'sunny' or 'rain':
                        found_array.append(['overcast', '?', '?', '?'])
                if entrenamiento[i][j] == 'hot' or 'mild' or 'cool':
                        found_array.append(['?', '?', '?', '?'])
                if entrenamiento[i][j] == 'high' or 'normal':
                        found_array.append(['?', '?', '?', '?'])
                if entrenamiento[i][j] == 'weak' or 'strong':
                        found_array.append(['?', '?', '?', '?'])

    false_array.append(g)
    false_array.append(found_array[:6])
    false_array.append(found_array[6:10])
    false_array.append(found_array[10:15])
    false_array.append(found_array[15:20])
    false_array.append(found_array[20:25])


    print('\n' + '****************Frontera más general********************' + '\n')
    print(false_array)
    return false_array


transform_especifica()
general()