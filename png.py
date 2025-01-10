bicycles = ['trek', 'cannondael', 'redline', 'specialized']
print()
print(bicycles)
print(bicycles[0].title())

bicycles[0] = 'heil'

print(bicycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print()
motorcycles.append('bmw')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)




motorcycles = ['honda', 'yamaha', 'suzuki']
poded = motorcycles.pop()
print(motorcycles)
print(poded)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f" Последняя покубка была аппарата {last_owned.title()}")
first_owned = motorcycles.pop(0)
print()
print(f"Первая покупка была {first_owned.title()}")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('yamaha')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expesive for me")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort(reverse=True)
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)
print(len(cars))
print()

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title())
print()
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a greet trick!")
	print(f"I can't wait to see your next  trick, {magician.title()}. \n")
print('Thanks you, everyone. That was a greet magic show !')


for value in range(1, 6):
	print(value)

numbers = list(range(1,11,2))
print(numbers)

squares = []
for value in range(1, 11):
	squares.append(value ** 2)

print(squares)



digits = list(range(1, 11))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))
squares = [value **2 for value in range(1, 11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:3])

my_food = ['pizza', 'falafel', 'carrot cake']
friend_food = my_food[:]
print(my_food)
print(friend_food)


dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dim in dimensions:
	print(dim)

cars = ['audio', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())

answer = 17
if answer !=42:
	print("That is  not the correct anser. Try again")

requested_topping = 'pulz'
if requested_topping != 'anchovies':
	print("Hold the anchovies")



print()

requested_topings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_topings:
	print("Джи джа")

if 'asas' in requested_topings:
	print("asas")


banned_users = ['andrew', 'carolina','david']
user = 'sasha'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish")
print()
toppings = ['mushrooms', 'green papers', 'extra cheese']
for top in toppings:
	if top == 'green paper':
		print("Sorry, we dont have a green paper")
	else:
		print(f"Adding {top.title()}")
print()
print("Finished making your pizza!")
print()

toppings = []
if toppings:
	for top in toppings:
		print(f"Adding {top.title()}")
	print("Finished making your pizza!")
else:
	print("Are you sure you want a plain pizza!")
print()
avaible_cars = ('bmw', 'merc', 'audi', 'panter')

request_cars = ['лада', 'приора', 'буханка', 'T-34']

for req in request_cars:
	if req in avaible_cars:
		print(f" Adding {req}")
	else:
		print(f"Sorry, we don't have {req}")

print("Finish")

alient = {'color': 'green', 'points': 5}
print(alient)
print(alient['color'])
print(alient['points'])

slovar = {}
slovar['x'] = 0
slovar['y'] = 25
print(slovar)
slovar['x'] = 100
print(slovar)

alinn_0 = {'x': 0, 'y': 1, 'speed':'medium'}
print(f"Original position: {alinn_0['x']}")

if alinn_0['speed'] == 'slow':
	x = 1
elif alinn_0['speed'] == 'medium':
	x = 2
else:
	x = 3
print()
alinn_0['x'] = alinn_0['x'] + x 
print(f"New position: {alinn_0['x']}")

print()


alinn_0 = {'x': 0, 'y': 1, 'speed':'medium'}
print(alinn_0)
del alinn_0['x']
print(alinn_0)

favorite_languages ={
	'alexander': 'python',
	'albert': 'java',
	'anastasia': 'c++',
}
print()
lang = favorite_languages['alexander']
print(F"Sasha favorute language is {lang.title()}")
print()

alient = {'color': 'green', 'points': 5}
pint = alient.get('olor', 'No data')
print(pint)


print()
user_0 = {
	'username': 'undead',
	'first': 'alexander',
	'last': 'voronkov',
}

for key, value in user_0.items():
	print(f"Key: {key}")
	print(f"Value: {value}")
print()

favorite_languages ={
	'alexander': 'python',
	'albert': 'java',
	'anastasia': 'c++',
}

for name, lang in favorite_languages.items():
	print(f"{name.title()} favorite language is {lang.title()}")

print()
favorite_languages ={
	'alexander': 'python',
	'albert': 'java',
	'anastasia': 'c++',
}

for key in favorite_languages.keys():
	print(key.title())
 


favorite_languages ={
	'alexander': 'python',
	'albert': 'java',
	'anastasia': 'c++',
}

friend = ['albert', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friend:
		lang = favorite_languages[name]
		print(f"\n{name.title()} your favor lang  is {lang.title()}")

if 'erwin' not in favorite_languages.keys():
	print("erwin, please take our pool")


for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for the taking the pool")


for val in favorite_languages.values():
	print(val)

for valu in set(favorite_languages.values()):
	print(valu)

alien0 = {'color': 'green', 'point': '1212'}
alien1 = {'color': 'yelow', 'point': '12'}
alien2 = {'color': 'green', 'point': '122'}

aliens = [alien1, alien0, alien2]

for va in aliens:
	print(va) 

aliens = []

for alien in range(30):
	new_aliens = {'color': 'green', 'points': 10, 'speed': 'slow'}
	aliens.append(new_aliens)

for alien in aliens[:5]:
	print(alien)

print(f"Total number of the aliens: {len(aliens)}")
print()



aliens = []

for ali in range(0,30):
	new = {'color': 'green', 'points': 1212, 'speed': 'slow'}
	aliens.append(new)

print(aliens)
print()
for ali in aliens[0:3]:
	if ali['color'] == 'green':
		ali['color'] = 'yellow'
		ali['spped'] = 'medium'
		ali['points'] = 10

for ali in aliens[0:5]:
	print(ali)



pizza = {
	'crust': 'thinks',
	'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You order a {pizza['crust']}- crust pizza")
for topp in pizza['toppings']:
	print("\t" + topp)

print(pizza['toppings'])




lub_lang = {
	'jen': ['python', 'ruby'],
	'alexander': ['python'],
	'edward': ['c++', 'ruby'],
	'phil': ['python', 'haskell'],
}

for name, language in lub_lang.items():
	print(f"\n {name.title()}")
	for lang in language:
		print(f"\t{lang.title()}")



users = {
	'undead':  {
		'firstname': 'alexander',
		'lastname': 'voronkov',
		'location': 'moskow',
		},
	'mcurie': {
		'firstname': 'marie',
		'lastname': 'curie',
		'location': 'paris',
		}
}

print(users)

for usr, info in users.items():
	print(f"\n Username: {usr.title()}")
	full_name = f"{info['firstname']} {info['lastname']}"
	location = f"{info['location']}"
	print(f"\tFullname: {full_name.title()}")
	print(f"\tLocation {location.title()}")




prompt = "if you us who are you, we can personalizae the message you see"
prompt += "\nWhat is your name  ?"
print(prompt)

current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1





n = 1 

while n <= 20:
	print(n)
	n += 1

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)


uncorfirmed_user = ['alice', 'brian', 'candace']
confirmed_users = []

while uncorfirmed_user:
	current = uncorfirmed_user.pop()

	print(f"Verifying user: {current}")
	confirmed_users.append(current)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())



def greet_user():
	"""Выводит простое приветствие"""
	print("Hello!:)")

greet_user()


def greet_user(username):
	print(f"Hello, {username.title()}")

greet_user('alex')


print()

def print_model(unprint, printed):
	"""Печать моделей"""
	while unprint:
		curr = unprint.pop()
		print(f"Printed model: {curr}")
		printed.append(curr)

def show_printed(printed):
	"""Показывает сделанные модели"""
	print("\nThe following models have been printed: ")
	for pri  in printed:
		print(pri)

unprinted = ['phone case', 'robot pendant', 'dodecahedron']
printed = []

print_model(unprinted, printed)
print(printed)

show_printed(printed)


def make_pizza(*toppings):
	"""Вывод списка заказных топингов"""
	print(toppings)

make_pizza('peperoni')
make_pizza('peperoni', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
	"""Вывод списка заказных топингов"""
	print("\nMaking a pizza with the following toppings: ")
	for top in toppings:
		print(f"- {top}")


make_pizza('peperoni')
make_pizza('peperoni', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
	"""Вывод списка заказных топингов"""
	print(f"\nMaking a {size} pizza with the following toppings: ")
	for top in toppings:
		print(f"- {top}")

make_pizza(16, 'peperoni')
make_pizza(28, 'peperoni', 'green peppers', 'extra cheese')

class Dog():
	"""Простая модель собаки """

	def __init__(self, name, age):
		"""Метод инициализирует атрибуты name и age"""
		self.name = name
		self.age  = age 

	def sit(self):
		"""Собака садиться по команде"""
		print(f"{self.name.title()} is now sitting.")

	def roll_over(self):
		"""Собака перекатывается по команде"""
		print(f"{self.name} rolled over!")


dog1 = Dog('max', 10)
print(dog1.name)
print(dog1.age)
dog1.sit()
dog1.roll_over()

your_dog = Dog('lucy', 3)
print(your_dog.name)
print(your_dog.age)
your_dog.sit()
your_dog.roll_over()

list1 = [1, 2, 4, 10, 121, 12]
list2 = [7, 77, 777]
list1.append(90)
list1.extend(list2)
print(list1)
print(list2)

class Restaurant():
	'''Класс описывающий ресторан'''
	def __init__(self, restaurant_name, cuisine_type):
	 	'''Инициализация атрибутов описания ресторана'''
	 	self.restaurant_name = restaurant_name
	 	self.cuisine_type = cuisine_type

	def describe_restaurant(self):
	 	'''Метод выводит атрибуты экземпляря'''
	 	print(f"{self.restaurant_name} {self.cuisine_type}")

	def open_restaurant(self):
	 	'''Выводит инфу о том что рестик открыт'''
	 	print(f"Restaurant {self.restaurant_name} is open! willkommen!")

restaurant = Restaurant('Cloude monet', 'air')
print(f"{restaurant.restaurant_name}")
print(f"{restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

class User():
	'''Describe user'''

	def __init__(self, first_name, last_name, age):
		'''Инициализация атрибутов пользователя'''
		self.first_name = first_name
		self.last_name = last_name
		self.age = age 

	def describe_user(self):
		'''Выводит инфу о пользователе'''
		full_name = f"{self.first_name} {self.last_name}"
		print(f"Fullname: {full_name} age: {self.age}")

	def great_user(self):
		'''Приветствует пользователя'''
		print(f"Hello, {self.first_name}")

alex = User('sasha', 'voron', '22')
print(f"{alex.first_name} {alex.age} ")
alex.describe_user()
alex.great_user()


class Car():
	'''Описание протого авто'''

	def __init__(self, make, model, year):
		'''Инициализация атрибутов описания авто'''
		self.make = make
		self.model = model 
		self.year = year 
		self.odometr_reading = 0

	def get_describe_name(self):
		'''Возвращает аккуратно отформатированное значение'''
		long_name =f"{self.make} {self.model} {self.year}"
		return long_name.title()

	def read_odometr(self):
		'''Выводит пробеш машины в метрах'''
		print(f"This car has {self.odometr_reading} miles on it")

	def update_odometr(self, mileage):
		'''Устанавливает заданное значение на одометре'''
		if mileage >= self.odometr_reading:
			self.odometr_reading = mileage
		else:
			print("You can't roll back an odometer")

	def increment_odometr(self, miles):
		'''Увеличивает показание с приращением'''
		self.odometr_reading += miles




new_car = Car('bmw', 'e90', '2002')
print(new_car.get_describe_name())
new_car.read_odometr()
new_car.odometr_reading = 25
new_car.read_odometr()
print()
new_car.update_odometr(23)
new_car.read_odometr()
print()

car2 = Car('subaru','outback', 2015)
print(car2.get_describe_name())
car2.update_odometr(23_500)
car2.read_odometr()

car2.increment_odometr(100)
car2.read_odometr()






class ElectricCar(Car):
	'''Представляет аспекты машины, спецефические для электромобилей'''

	def __init__(self, year, model, make):
		'''инициализирует атрибуты класса родителя'''

		super().__init__(make, model, year)
		self.battery_size = 75

	def describe_battery(self):
		'''Выводит инфу о мощности акумулятора'''
		print(f"This car has a {self.battery_size}-kWh battery")

my_tesla = ElectricCar('tesla', 'model`s', '2019')
print(my_tesla.get_describe_name())
my_tesla.describe_battery()