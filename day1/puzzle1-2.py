import numpy as np

data = np.loadtxt('/Users/student/cs/advent_of_code/day1/data1.txt')

list1 = data[:, 0]
list2 = data[:, 1]

freq = {}

for elem in list2:
  if elem not in freq.keys():
    freq[elem] = 0
  freq[elem] += 1

sum = 0
for item in list1:
  if item not in freq.keys():
    freq[item] = 0
  sum += item * freq[item]

print(sum)