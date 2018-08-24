import csv
with open ('1.csv','rb') as csvfile:
	a=['sdfg','asgg','gfsf']
	my_reader = csv.reader(csvfile, delimiter=' ', quotechar ='|')
	if 'asgg' in a:
		my_reader.append("asgg")
	for row in my_reader:
		for item in row:
			print(item)