
def name_function(name, last_name, middle = ''):
	'''Функция получает имя и фамилию и формарует полное имя'''
	if middle:
		full_name = f"{last_name} {name} {middle}"
	else:
		full_name = f"{last_name} {name}"

	return full_name
	