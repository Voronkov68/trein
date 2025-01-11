from random import randint, choice
from car import ElectricCar, Car

new_nesla = ElectricCar('tesla', 'model s', '2019')
new_nesla.battery.describe_battery()
new_nesla.battery.get_range()

car = Car('bmw', 'beetle', '2019')
print(car.get_describe_name())

print()
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(randint(1, 10))
print(choice(players))