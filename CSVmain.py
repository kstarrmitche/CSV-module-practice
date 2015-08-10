import csv #this module (bits of code) allows to manipulate csv files with already written functions
l = []
l2 = []

def readcsvfile(str):
	with open(str, 'r') as r:
		reader = csv.reader(r)
		for row in r:
			print(row)

def getInputFromFile(str):
	with open(str, 'r', encoding='utf-8') as a_file:
		for line in a_file:
			l.append(line.rstrip())

def writecsvfile(str):
	getInputFromFile('ingre.txt')
	with open(str, 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=' ')
		for item in l:
			spamwriter.writerow(item)

def main():
	writecsvfile('Ingredients.csv')

main()