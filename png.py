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
