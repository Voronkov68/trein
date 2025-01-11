from car import Car 

new_car = Car('audi', 'a4', '2019')
print(new_car.get_describe_name())
new_car.odometer_reading = 23
new_car.read_odometr()