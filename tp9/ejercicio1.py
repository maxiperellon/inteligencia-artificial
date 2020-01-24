data = [
     {'outlook': 'sunny', 'temperature': 'hot', 'humidity': 'high', 'wind': 'weak', 'play_tennis': 'False'},
     {'outlook': 'sunny', 'temperature': 'hot', 'humidity': 'high', 'wind': 'strong', 'play_tennis': 'False'},
     {'outlook': 'overcast', 'temperature': 'hot', 'humidity': 'high', 'wind': 'weak', 'play_tennis': 'True'},
     {'outlook': 'rain', 'temperature': 'mild', 'humidity': 'high', 'wind': 'weak', 'play_tennis': 'True'},
     {'outlook': 'rain', 'temperature': 'cool', 'humidity': 'normal', 'wind': 'weak', 'play_tennis': 'True'},
     {'outlook': 'rain', 'temperature': 'cool', 'humidity': 'normal', 'wind': 'strong', 'play_tennis': 'False'},
     {'outlook': 'overcast', 'temperature': 'cool', 'humidity': 'normal', 'wind': 'strong', 'play_tennis': 'True'},
     {'outlook': 'sunny', 'temperature': 'mild', 'humidity': 'high', 'wind': 'weak', 'play_tennis': 'False'},
     {'outlook': 'sunny', 'temperature': 'cool', 'humidity': 'normal', 'wind': 'weak', 'play_tennis': 'True'},
     {'outlook': 'rain', 'temperature': 'mild', 'humidity': 'normal', 'wind': 'weak', 'play_tennis': 'True'},
     {'outlook': 'sunny', 'temperature': 'mild', 'humidity': 'normal', 'wind': 'strong', 'play_tennis': 'True'},
     {'outlook': 'overcast', 'temperature': 'mild', 'humidity': 'high', 'wind': 'strong', 'play_tennis': 'True'},
     {'outlook': 'overcast', 'temperature': 'hot', 'humidity': 'normal', 'wind': 'weak', 'play_tennis': 'True'},
     {'outlook': 'rain', 'temperature': 'mild', 'humidity': 'high', 'wind': 'strong', 'play_tennis': 'False'}
]

total = len(data)

# Funciones generales
def contar_general(value):
	def contar(palabra):
		cont = 0
		for i in data:
			if i[value]==palabra:
				cont += 1
		return cont

	data_gen = []
	def data2(palabra):
		for i in data_gen:
			if i[value]==palabra:
				return True
		return False            

	for i in data:
		if contar(i[value])>0 and data2(i[value])==False:
			data_gen.append({value: i[value], 'cant': contar(i[value])})
	return data_gen

def filtrar_true_false(value1, value2):
	datalist = []
	for x in data:
		cont = data.count(x)
		if cont > 0:
			element = {}
			element[value1] = x[value1]
			element[value2] = x[value2]
			datalist.append(element)

	new_datalist = []
	for x in datalist:
		e_cont = datalist.count(x)
		if e_cont > 0:
			new_element = {}
			new_element[value1] = x[value1]
			new_element[value2] = x[value2]
			new_element['cant'] = e_cont
			new_datalist.append(new_element)

	seen = set()
	new_l = []
	for d in new_datalist:
		t = tuple(d.items())
		if t not in seen:
			seen.add(t)
			new_l.append(d)
	return new_l

def prob_class(true, false, total):
    prob_true = true/total
    prob_false = false/total
    return prob_true, prob_false

#PLAYTENNIS
def data_play_tennis():
    return contar_general('play_tennis')
    
true = data_play_tennis()[1]['cant']
false = data_play_tennis()[0]['cant']  

prob_true_false = prob_class(true, false, total)

print('Probabilidad a priori de cada clase: ')
print('Probabilidad de True: ', prob_true_false[0])
print('Probabilidad de False: ', prob_true_false[1])

#OUTLOOK
def data_outlook():
	return contar_general('outlook')
	
def data_outlook_true_false():
	return filtrar_true_false('outlook', 'play_tennis')

#Probabilidad de sunny
true_sunny = data_outlook_true_false()[4]['cant']
false_sunny = data_outlook_true_false()[0]['cant']

prob_sunny_true = true_sunny/true
prob_sunny_false = false_sunny/false

print('Probabilidad de que sunny sea True: ', prob_sunny_true)
print('Probabilidad de que sunny sea False: ', prob_sunny_false)

#Probabilidad de overcast
true_overcast = data_outlook_true_false()[1]['cant']
false_overcast = 0

prob_overcast_true = true_overcast/true
prob_overcast_false = false_overcast/false

print('Probabilidad de que overcast sea True: ', prob_overcast_true)
print('Probabilidad de que overcast sea False: ', prob_overcast_false)

#Probabilidad de rain
true_rain = data_outlook_true_false()[2]['cant']
false_rain = data_outlook_true_false()[3]['cant']

prob_rain_true = true_rain/true
prob_rain_false = false_rain/false

print('Probabilidad de que rain sea True: ', prob_rain_true)
print('Probabilidad de que rain sea False: ', prob_rain_false)

#TEMPERATURE
def data_temperature():
	return contar_general('temperature')

def data_temp_true_false():
	return filtrar_true_false('temperature', 'play_tennis')





