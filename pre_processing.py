import csv

filereader = open("labeled_data.csv", 'r')
f = csv.reader(filereader)
filewriter = open("dataset.csv", "w")
w = csv.writer(filewriter)
for row in f:
    num = 0
    if row[5] == '0' or row[5] == '1':
        num = 1
    w.writerow([num, row[6]])
