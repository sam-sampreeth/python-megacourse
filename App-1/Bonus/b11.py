def getAvg():
    with open('subfiles/b11data.txt', 'r') as file:
        data = file.readlines()
    vals = data[1:]
    vals = [float(i) for i in vals]
    average = sum(vals) / len(vals)
    return average


avg = getAvg()
print(avg)
