import json

with open('newfile.txt') as f:
	files = json.load(f)

print(files)