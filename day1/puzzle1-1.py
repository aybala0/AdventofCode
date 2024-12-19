
import numpy as np
data = np.loadtxt('/Users/student/cs/advent_of_code/day1/data1.txt')
sorteddata = np.sort(data, axis=0)
print(sorteddata)
sum = 0
for row in sorteddata:
  sum += abs(row[0] - row[1])

print(sum)
    