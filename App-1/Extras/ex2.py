import csv

with open("../files/one.csv", 'r') as f:
    data = list(csv.reader(f))

row = input("Enter row: ")
for i in data:
    if i[0] == row:
        print(i[1])