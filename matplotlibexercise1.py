import csv
import statistics
import numpy as np
import matplotlib.pyplot as plt

with open('activity.csv', 'r') as f:
    data = csv.reader(f)
    mydict = {}
    for row in data:
        if row[0] != 'NA' and row[0] != 'steps':
            if row[1] not in mydict:
                mydict[row[1]] = [int(row[0])]
            else:
                mydict[row[1]].append(int(row[0]))

#print(mydict)

totalperday = {}
mean_totalperday = {}
median_perday = {}
for key, value in mydict.items():
    totalperday[key] = sum(value)
    mean_totalperday[key] = round(statistics.mean(value),2)
    median_perday[key] = statistics.median(value)

print(totalperday)
#print(mean_totalperday)
#print(median_perday)

#graph
N = len(mydict)
meantotalperday = tuple(mean_totalperday.values())
ind = np.arange(N)    # the x locations for the groups
width = 0.8       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, meantotalperday, width)

plt.ylabel('Steps')
plt.title('Mean Total Step per Day')
plt.xticks(ind, tuple(mean_totalperday.keys()))
plt.yticks(np.arange(0, 101, 20))

#plt.show()