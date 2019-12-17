import csv
import statistics
import numpy as np
import matplotlib.pyplot as plt

with open('activity.csv', 'r') as f:
    data = csv.reader(f)
    mydict = {}
    for row in data:
        if row[0] != 'NA' and row[0] != 'steps':
            if row[2] not in mydict:
                mydict[row[2]] = [int(row[0])]
            else:
                mydict[row[2]].append(int(row[0]))

print(mydict)

totalpertime = {}
mean_totalpertime = {}
median_pertime = {}
for key, value in mydict.items():
    totalpertime[key] = sum(value)
    mean_totalpertime[key] = round(statistics.mean(value),2)

#print(totalpertime)
#print(mean_totalpertime)

#graph
plt.plot(list(mean_totalpertime.keys()), list(mean_totalpertime.values()))
plt.xlabel('time')
plt.ylabel('steps each 5 time')
plt.show()

#plt.plot([semua x value], [semua y value])