

filename = 'pi.txt'

with open(filename) as f:
	lines = f.readlines()   
print(lines)
pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))  


try:
	print(3 / 0)
except ZeroDivisionError:
	print('You can t divide by zero')