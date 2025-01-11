"""Класс для представлении автомобиля c бензиновым и электродвигателем"""




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

	def full_gas_tank(self):
		'''Заправка авто'''
		print('Машина заправляеться')


class Battery():
	'''Простая модель акума авто'''

	def __init__(self, battery_size=75):
		self.battery_size = battery_size


	def describe_battery(self):
		'''Выводит инфу о мощности акумулятора'''
		print(f"This car has a {self.battery_size}-kWh battery")

	def get_range(self):
		'''Выводит приблизительный запас хода'''
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge.")



class ElectricCar(Car):
	'''Представляет аспекты машины, спецефические для электромобилей'''

	def __init__(self, year, model, make):
		'''инициализирует атрибуты класса родителя'''

		super().__init__(make, model, year)
		self.battery = Battery()

	

	def full_gas_tank(self):
		'''Заправки нет'''
		print('This car doesn t need a gas tank!')



