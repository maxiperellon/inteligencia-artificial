#Casado - Fiochetti - Perellón

from math import log2

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

def filtrar_true_false2(value1, value2, value3):
	datalist = []
	for x in data:
		cont = data.count(x)
		if cont > 0:
			element = {}
			element[value1] = x[value1]
			element[value2] = x[value2]
			element[value3] = x[value3]
			datalist.append(element)

	new_datalist = []
	for x in datalist:
		e_cont = datalist.count(x)
		if e_cont > 0:
			new_element = {}
			new_element[value1] = x[value1]
			new_element[value2] = x[value2]
			new_element[value3] = x[value3]
			new_element['cant'] = e_cont
			new_datalist.append(new_element)

	seen = set()
	new_l = []
	for d in new_datalist:
		t = tuple(d.items())
		if t not in seen:
			seen.add(t)
			new_l.append(d)
	
	new_list = sorted(new_l, key=lambda k: k['outlook'])
	return new_list

#PLAYTENNIS
def contar_true_and_false(palabra):
    cont_true_false = 0
    for i in data:
        if i['play_tennis']==palabra:
            cont_true_false += 1
    return cont_true_false

data_true_false = []
def true_false_en_data2(palabra):
    for i in data_true_false:
        if i['play_tennis']==palabra:
            return True
    return False            

for i in data:
    if contar_true_and_false(i['play_tennis'])>1 and true_false_en_data2(i['play_tennis'])==False:
        data_true_false.append({'play_tennis': i['play_tennis'], 'cant': contar_true_and_false(i['play_tennis'])})

#OUTLOOK
def data_outlook():
	data_outlook = contar_general('outlook')
	return data_outlook
	
def data_outlook_true_false():
	data_true_false = filtrar_true_false('outlook', 'play_tennis')
	return data_true_false

print(data_outlook_true_false())


#TEMPERATURE
def data_temperature():
	data_temp = contar_general('temperature')
	return data_temp

def data_temp_true_false():
	data_true_false = filtrar_true_false('temperature', 'play_tennis')
	return data_true_false

#HUMIDITY
def data_humidity():
	data_hum = contar_general('humidity')
	return data_hum

def data_hum_true_false():
	data_true_false = filtrar_true_false('humidity', 'play_tennis')
	return data_true_false

#WIND
def data_wind():
	data_wind = contar_general('wind')
	return data_wind

def data_wind_true_false():
	data_true_false = filtrar_true_false('wind', 'play_tennis')
	return data_true_false

#Entropia del sistema
def entropia_del_sistema():
	no = data_true_false[0]['cant']
	yes = data_true_false[1]['cant']
	entropia_inicial = - (yes/total)*log2(yes/total) - (no/total)*log2(no/total)
	return entropia_inicial

#Entropias
def entropia(value1, total):
	if value1 != 0:
		entropia = -(value1/total)*log2(value1/total)
	else:
		entropia = 0
	return entropia

#entropia de sunny
total_sunny = data_outlook()[0]['cant']
prob_sunny = total_sunny/total
def entropia_sunny():
	#sunny
	true_sunny = data_outlook_true_false()[4]['cant']
	false_sunny = data_outlook_true_false()[0]['cant']
	e_sunny = entropia(true_sunny, total_sunny) + entropia(false_sunny, total_sunny)
	return e_sunny

#entropia de overcast
total_overcast = data_outlook()[1]['cant']
prob_overcast = total_overcast/total
def entropia_overcast():
	#overcast
	true_overcast = data_outlook_true_false()[1]['cant']
	false_overcast = 0
	e_overcast = entropia(true_overcast, total_overcast) + entropia(false_overcast, total_overcast) 
	return e_overcast

#entropia de rain
total_rain = data_outlook()[2]['cant']
prob_rain = total_rain/total
def entropia_rain():
	#rain
	true_rain = data_outlook_true_false()[2]['cant']
	false_rain = data_outlook_true_false()[3]['cant']
	e_rain = entropia(true_rain, total_rain) + entropia(false_rain, total_rain)
	return e_rain

#entropia de hot
total_hot = data_temperature()[0]['cant']
prob_hot = total_hot/total
def entropia_hot():
	#hot
	true_hot = data_temp_true_false()[1]['cant']
	false_hot = data_temp_true_false()[0]['cant']
	e_hot = entropia(true_hot, total_hot) + entropia(false_hot, total_hot)
	return e_hot

#entropia de mild
total_mild = data_temperature()[1]['cant']
prob_mild = total_mild/total
def entropia_mild():
	#mild
	true_mild = data_temp_true_false()[2]['cant']
	false_mild = data_temp_true_false()[5]['cant']
	e_mild = entropia(true_mild, total_mild) + entropia(false_mild, total_mild)
	return e_mild

#entropia de cool
total_cool = data_temperature()[2]['cant']
prob_cool = total_cool/total 
def entropia_cool():
	#cool
	true_cool = data_temp_true_false()[3]['cant']
	false_cool = data_temp_true_false()[4]['cant']
	e_cool = entropia(true_cool, total_cool) + entropia(false_cool, total_cool)
	return e_cool

#entropia de high
total_high = data_humidity()[0]['cant']
prob_high = total_high/total
def entropia_high():
	#high	
	true_high = data_hum_true_false()[1]['cant']
	false_high = data_hum_true_false()[0]['cant']
	e_high = entropia(true_high, total_high) + entropia(false_high, total_high)
	return e_high

#entropia de normal
total_normal = data_humidity()[1]['cant']
prob_normal = total_normal/total
def entropia_normal():
	#normal
	true_normal = data_hum_true_false()[2]['cant']
	false_normal = data_hum_true_false()[3]['cant']
	e_normal = entropia(true_normal, total_normal) + entropia(false_normal, total_normal)
	return e_normal

#entropia de weak
total_weak = data_wind()[0]['cant']
prob_weak = total_weak/total
def entropia_weak():	
	#weak
	true_weak = data_wind_true_false()[2]['cant']
	false_weak = data_wind_true_false()[0]['cant']
	e_weak = entropia(true_weak, total_weak) + entropia(false_weak, total_weak) 
	return e_weak

#entropia de strong
total_strong = data_wind()[1]['cant']
prob_strong = total_strong/total
def entropia_strong():
	#strong
	true_strong = data_wind_true_false()[3]['cant']
	false_strong = data_wind_true_false()[1]['cant']
	e_strong = entropia(true_strong, total_strong) + entropia(false_strong, total_strong) 
	return e_strong

#Ganancia de Outlook
def ganancia_outlook():
	e_sist = entropia_del_sistema()
	e_sunny = entropia_sunny()
	e_overcast = entropia_overcast()
	e_rain = entropia_rain()

	g_outlook = e_sist - (prob_sunny*e_sunny + prob_overcast*e_overcast + prob_rain*e_rain) 
	return g_outlook

#Ganancia de Temperature
def ganancia_temperature():
	e_sist = entropia_del_sistema()
	e_hot = entropia_hot()
	e_mild = entropia_mild()
	e_cool = entropia_cool()

	g_temp = e_sist - (prob_hot*e_hot + prob_mild*e_mild + prob_cool*e_cool)
	return g_temp

#Ganancia de Humidity
def ganancia_humidity():
	e_sist = entropia_del_sistema()
	e_high = entropia_high()
	e_normal = entropia_normal()
	
	g_hum = e_sist - (prob_high*e_high + prob_normal*e_normal)
	return g_hum

#Ganancia de Wind
def ganancia_wind():
	e_sist = entropia_del_sistema()
	e_weak = entropia_weak()
	e_strong = entropia_strong()
	
	g_wind = e_sist - (prob_weak*e_weak + prob_strong*e_strong)
	return g_wind

def outlook_temp():
	out_temp = filtrar_true_false2('outlook', 'temperature', 'play_tennis')
	return out_temp

overcast_temp = outlook_temp()[0:3]
rain_temp = outlook_temp()[3:7]
sunny_temp = outlook_temp()[7:11]

# print(overcast_temp)
# print(rain_temp)
# print(sunny_temp)

def outlook_hum():
	out_hum = filtrar_true_false2('outlook', 'humidity', 'play_tennis')
	return out_hum

overcast_hum = outlook_hum()[0:2]
rain_hum = outlook_hum()[2:6]
sunny_hum = outlook_hum()[6:8]

# print(overcast_hum)
# print(rain_hum)
# print(sunny_hum)

def outlook_wind():
	out_wind = filtrar_true_false2('outlook', 'wind', 'play_tennis')
	return out_wind

overcast_wind = outlook_wind()[0:2]
rain_wind = outlook_wind()[2:4]
sunny_wind = outlook_wind()[4:8]

# print(overcast_wind)
# print(rain_wind)
# print(sunny_wind)

#Ganancia de sunny (temperature)
def ganancia_sunny_temp():
	e_sunny = entropia_sunny()
	#sunny-hot
	hot_true = 0
	hot_false = sunny_temp[0]['cant']
	hot_total = hot_true + hot_false
	hot_prob = hot_total/total_sunny
	e_hot = entropia(hot_true, hot_total) +  entropia(hot_false, hot_total)
	
	#sunny-mild
	mild_true = sunny_temp[3]['cant']
	mild_false = sunny_temp[1]['cant']
	mild_total = mild_true + mild_false
	mild_prob = mild_total/total_sunny
	e_mild = entropia(mild_true, mild_total) +  entropia(mild_false, mild_total)
	
	#sunny-cool
	cool_true = sunny_temp[2]['cant']
	cool_false = 0
	cool_total = cool_true + cool_false
	cool_prob = cool_total/total_sunny
	e_cool = entropia(cool_true, cool_total) +  entropia(cool_false, cool_total)
	
	g_sunny_temp = e_sunny - (hot_prob*e_hot + mild_prob*e_mild + cool_prob*e_cool)
	return g_sunny_temp

#Ganancia de sunny (humidity)
def ganancia_sunny_hum():
	e_sunny = entropia_sunny()
	#sunny-high
	high_true = 0
	high_false = sunny_hum[0]['cant']
	high_total = high_true + high_false
	high_prob = high_total/total_sunny
	e_high = entropia(high_true, high_total) +  entropia(high_false, high_total)
	
	#sunny-normal
	normal_true = sunny_hum[1]['cant']
	normal_false = 0
	normal_total = normal_true + normal_false
	normal_prob = normal_total/total_sunny
	e_normal = entropia(normal_true, normal_total) +  entropia(normal_false, normal_total)
	
	g_sunny_hum = e_sunny - (high_prob*e_high + normal_prob*e_normal)
	return g_sunny_hum

#Ganancia de sunny (wind)
def ganancia_sunny_wind():
	e_sunny = entropia_sunny()
	#sunny-weak
	weak_true = sunny_wind[2]['cant']
	weak_false = sunny_wind[0]['cant']
	weak_total = weak_true + weak_false
	weak_prob = weak_total/total_sunny
	e_weak = entropia(weak_true, weak_total) +  entropia(weak_false, weak_total)
	
	#sunny-strong
	strong_true = sunny_wind[1]['cant']
	strong_false = sunny_wind[1]['cant']
	strong_total = strong_true + strong_false
	strong_prob = strong_total/total_sunny
	e_strong = entropia(strong_true, strong_total) +  entropia(strong_false, strong_total)
	
	g_sunny_wind = e_sunny - (weak_prob*e_weak + strong_prob*e_strong)
	return g_sunny_wind

#Ganancia de overcast (temperature)
def ganancia_overcast_temp():
	e_overcast = entropia_overcast()
	#overcast-hot
	hot_true = overcast_temp[0]['cant']
	hot_false = 0
	hot_total = hot_true + hot_false
	hot_prob = hot_total/total_overcast
	e_hot = entropia(hot_true, hot_total) +  entropia(hot_false, hot_total)
	
	#overcast-mild
	mild_true = overcast_temp[2]['cant']
	mild_false = 0
	mild_total = mild_true + mild_false
	mild_prob = mild_total/total_overcast
	e_mild = entropia(mild_true, mild_total) +  entropia(mild_false, mild_total)
	
	#overcast-cool
	cool_true = overcast_temp[1]['cant']
	cool_false = 0
	cool_total = cool_true + cool_false
	cool_prob = cool_total/total_overcast
	e_cool = entropia(cool_true, cool_total) +  entropia(cool_false, cool_total)
	
	g_overcast_temp = e_overcast - (hot_prob*e_hot + mild_prob*e_mild + cool_prob*e_cool)
	return g_overcast_temp

#Ganancia de overcast (humidity)
def ganancia_overcast_hum():
	e_overcast = entropia_overcast()
	#overcast-high
	high_true = overcast_hum[0]['cant']
	high_false = 0
	high_total = high_true + high_false
	high_prob = high_total/total_overcast
	e_high = entropia(high_true, high_total) +  entropia(high_false, high_total)
	
	#overcast-normal
	normal_true = overcast_hum[1]['cant']
	normal_false = 0
	normal_total = normal_true + normal_false
	normal_prob = normal_total/total_overcast
	e_normal = entropia(normal_true, normal_total) +  entropia(normal_false, normal_total)
	
	g_overcast_hum = e_overcast - (high_prob*e_high + normal_prob*e_normal)
	return g_overcast_hum

#Ganancia de overcast (wind)
def ganancia_overcast_wind():
	e_overcast = entropia_overcast()
	#overcast-weak
	weak_true = overcast_wind[0]['cant']
	weak_false = 0
	weak_total = weak_true + weak_false
	weak_prob = weak_total/total_overcast
	e_weak = entropia(weak_true, weak_total) +  entropia(weak_false, weak_total)
	
	#overcast-strong
	strong_true = sunny_wind[1]['cant']
	strong_false = 0
	strong_total = strong_true + strong_false
	strong_prob = strong_total/total_overcast
	e_strong = entropia(strong_true, strong_total) +  entropia(strong_false, strong_total)
	
	g_overcast_wind = e_overcast - (weak_prob*e_weak + strong_prob*e_strong)
	return g_overcast_wind

#Ganancia de rain (temperature)
def ganancia_rain_temp():
	e_rain = entropia_rain()
	#rain-hot
	hot_true = 0
	hot_false = 0
	hot_total = hot_true + hot_false
	hot_prob = hot_total/total_rain
	e_hot = entropia(hot_true, hot_total) +  entropia(hot_false, hot_total)
	
	#rain-mild
	mild_true = rain_temp[0]['cant']
	mild_false = rain_temp[3]['cant']
	mild_total = mild_true + mild_false
	mild_prob = mild_total/total_rain
	e_mild = entropia(mild_true, mild_total) +  entropia(mild_false, mild_total)
	
	#rain-cool
	cool_true = rain_temp[1]['cant']
	cool_false = rain_temp[2]['cant']
	cool_total = cool_true + cool_false
	cool_prob = cool_total/total_sunny
	e_cool = entropia(cool_true, cool_total) +  entropia(cool_false, cool_total)
	
	g_rain_temp = e_rain - (hot_prob*e_hot + mild_prob*e_mild + cool_prob*e_cool)
	return g_rain_temp

#Ganancia de rain (humidity)
def ganancia_rain_hum():
	e_rain = entropia_rain()
	#sunny-high
	high_true = rain_hum[0]['cant']
	high_false = rain_hum[3]['cant']
	high_total = high_true + high_false
	high_prob = high_total/total_sunny
	e_high = entropia(high_true, high_total) + entropia(high_false, high_total)
	
	#sunny-normal
	normal_true = rain_hum[1]['cant']
	normal_false = rain_hum[2]['cant']
	normal_total = normal_true + normal_false
	normal_prob = normal_total/total_sunny
	e_normal = entropia(normal_true, normal_total) +  entropia(normal_false, normal_total)
	
	g_rain_hum = e_rain - (high_prob*e_high + normal_prob*e_normal)
	return g_rain_hum


#Ganancia de rain (wind)
def ganancia_rain_wind():
	e_rain = entropia_rain()
	#sunny-weak
	weak_true = rain_wind[0]['cant']
	weak_false = 0
	weak_total = weak_true + weak_false
	weak_prob = weak_total/total_sunny
	e_weak = entropia(weak_true, weak_total) +  entropia(weak_false, weak_total)
	
	#sunny-strong
	strong_true = 0
	strong_false = rain_wind[1]['cant']
	strong_total = strong_true + strong_false
	strong_prob = strong_total/total_sunny
	e_strong = entropia(strong_true, strong_total) +  entropia(strong_false, strong_total)
	
	g_rain_wind = e_rain - (weak_prob*e_weak + strong_prob*e_strong)
	return g_rain_wind

print('GANANCIAS..')
print('********************************************************')
print('Ganancia Outlook: ', ganancia_outlook())
print('Ganancia Temperature: ', ganancia_temperature())
print('Ganancia Humidity: ', ganancia_humidity())
print('Ganancia Wind: ', ganancia_wind())
print('********************************************************')
print('Ganancia Sunny-Temperature: ', ganancia_sunny_temp())
print('Ganancia Sunny-Humidity: ', ganancia_sunny_hum())
print('Ganancia Sunny-Wind: ', ganancia_sunny_wind())
print('********************************************************')
print('Ganancia Overcast-Temperature: ', ganancia_overcast_temp())
print('Ganancia Overcast-Humidity: ', ganancia_overcast_hum())
print('Ganancia Overcast-Wind: ', ganancia_overcast_wind())
print('********************************************************')
print('Ganancia Rain-Temperature: ', ganancia_rain_temp())
print('Ganancia Rain-Humidity: ', ganancia_rain_hum())
print('Ganancia Rain-Wind: ', ganancia_rain_wind())
print('********************************************************')

def arbol_final():	
	max_ganancia = max(ganancia_outlook(), ganancia_temperature(), ganancia_humidity(), ganancia_wind())
	print('\nGenerando árbol...\n')
	if ganancia_outlook() == max_ganancia:
		print('> outlook')
	elif ganancia_temperature() == max_ganancia:
		print('> temperature')
	elif ganancia_humidity() == max_ganancia:
		print('> humidity')
	elif ganancia_wind() == max_ganancia:
		print('> wind')
	
	max_gan_sunny = max(ganancia_sunny_temp(), ganancia_sunny_hum(), ganancia_sunny_wind())
	print('>> sunny' + ' --> sale de outlook')
	if ganancia_sunny_temp() == max_gan_sunny:
		print('>>> temperature' + ' --> sale de sunny')
	elif ganancia_sunny_hum() == max_gan_sunny:
		print('>>> humidity' + ' --> sale de sunny')
	elif ganancia_sunny_wind() == max_gan_sunny:
		print('>>> wind' + ' --> sale de sunny')
	
	max_gan_overcast = max(ganancia_overcast_temp(), ganancia_overcast_hum(), ganancia_overcast_wind())
	print('>> overcast' + ' --> sale de outlook')
	if ganancia_overcast_temp() != max_gan_overcast:
		print('>>> temperature' + ' --> sale de overcast')
	elif ganancia_overcast_hum() != max_gan_overcast:
		print('>>> humidity' + ' --> sale de overcast')
	elif ganancia_overcast_wind() != max_gan_overcast:
		print('>>> wind' + ' --> sale de overcast')

	max_gan_rain = max(ganancia_rain_temp(), ganancia_rain_hum(), ganancia_rain_wind())
	print('>> rain' + ' --> sale de outlook')
	if ganancia_rain_temp() == max_gan_rain:
		print('>>> temperature' + ' --> sale de rain')
	elif ganancia_rain_hum() == max_gan_rain:
		print('>>> humidity' + ' --> sale de rain')
	elif ganancia_rain_wind() == max_gan_rain:
		print('>>> wind' + ' --> sale de rain')
	
arbol_final()