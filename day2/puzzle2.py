import numpy as np 


def issafe(lst: list[int]):
  if len(lst) < 2:
    return True

  increasing = False
  if lst[0] < lst[1]:
    increasing = True
  l = len(lst)
  for i in range(l - 1):
    difference = lst[i+1] - lst[i] 
    if increasing:
      if(difference > 3 or difference < 1):
        return False
    else:
      if(difference < -3 or difference > -1):
        return False

  return True

def issafe2(lst: list[int], tolerant = True):
  if len(lst) < 2:
    return True

  increasing = False
  if lst[0] < lst[1]:
    increasing = True
  l = len(lst)
  
  for i in range(l - 1):
    difference = lst[i+1] - lst[i] 
    if increasing:
      if(difference > 3 or difference < 1):
        if tolerant:
          for j in range(l):
            newlist = lst[:]

            del newlist[j]
            if issafe2(newlist, False):
              return True
          return False

        return False
        
    else:
      if(difference < -3 or difference > -1):
        if tolerant:
          for j in range(l):
            newlist = lst[:]

            del newlist[j]
            if issafe2(newlist, False):
              return True
          return False
        return False

  return True


sum = 0
with open('/Users/student/cs/advent_of_code/day2/data1.txt', 'r') as file:
  for line in file:
    row = list(map(int, line.strip().split(" ")))
    if issafe2(row):
      sum += 1
    else:
      print(row)

print(sum)
