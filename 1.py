import json



name = input('Введите св')
with open('newfile.txt', 'a') as f:
	json.dump('helo', f)





