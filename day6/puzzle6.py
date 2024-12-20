import copy
import time

data = []

with open('/Users/student/cs/advent_of_code/day6/data.txt') as file:
  for line in file:
    row = [x for x in line.strip()]
    data.append(row)


def find_guard(matrix):
  for i, row in enumerate(matrix):
    for j, val in enumerate(row):
      if val == '^':
        return (i, j)

def next_step(i, j, direction):
  if direction == 0:
    return (i-1, j)
  elif direction == 1:
    return (i, j+1)
  elif direction == 2:
    return (i+1, j)
  elif direction == 3:
    return (i, j-1)

def print_matrix(matrix):
  for row in matrix:
    for val in row:
      print(val, end="")
    print()

#for the first part
def path(matrix):
  area = copy.deepcopy(matrix)

  corners = set()
  i, j = find_guard(data)

  rows = len(area)
  cols = len(area[0])
  direction = 0 #0 for up, 1 for right, 2 for down, 3 for left
  sum = 0
  try_i, try_j = next_step(i, j, direction)
  while try_i < rows and try_j < cols:
    if area[try_i][try_j] != '#':
      
      i = try_i
      j = try_j
      if area[try_i][try_j] == '.':
        area[i][j] = "X"
        sum += 1
    else:
      direction = (direction + 1) % 4
      corners.add((i, j))
    try_i, try_j = next_step(i, j, direction)
  
  return sum + 1


def findcorners(matrix):
  area = copy.deepcopy(matrix)

  corners = []
  i, j = find_guard(data)

  rows = len(area)
  cols = len(area[0])
  direction = 0 #0 for up, 1 for right, 2 for down, 3 for left
  sum = 0
  try_i, try_j = next_step(i, j, direction)
  while try_i < rows and try_j < cols:
    if area[try_i][try_j] != '#':
      
      i = try_i
      j = try_j
      if area[try_i][try_j] == '.':
        area[i][j] = "X"
        sum += 1
    else:
      direction = (direction + 1) % 4
      corners.append((i, j))
    try_i, try_j = next_step(i, j, direction)

  return corners



def findpaths(matrix):
  area = copy.deepcopy(matrix)

  paths = []
  i, j = find_guard(data)

  rows = len(area)
  cols = len(area[0])
  direction = 0 #0 for up, 1 for right, 2 for down, 3 for left
  sum = 0
  try_i, try_j = next_step(i, j, direction)
  newpath = []
  while try_i < rows and try_j < cols:
    if area[try_i][try_j] != '#':
      i = try_i
      j = try_j
      newpath.append((i, j))
      if area[try_i][try_j] == '.':
        area[i][j] = "X"
        sum += 1
    else:
      paths.append(newpath)
      newpath = []
      newpath.append((i, j))
      direction = (direction + 1) % 4
    try_i, try_j = next_step(i, j, direction)
  paths.append(newpath)
  return paths

def count(matrix):
  paths = findpaths(matrix)
  corners = findcorners(matrix)

  sum = 0

  for c in range(len(corners)):
    for p in range(c+1, len(paths)):
      if p%4 == ((c%4)+3)%4:
        i, j = corners[c]
    
        for loc in paths[p]:
          row, col = loc
          if c%2 == 1 and i == row:
            print("found",row, col)
            sum += 1
          if c%2 == 0 and j == col:
            sum += 1
            print("found",row, col)

  return sum



def brute_force(matrix):
  area = copy.deepcopy(matrix)
  paths = findpaths(matrix)
  sum = set()
  for path in paths:
    for pos in path:
      i, j = pos
      if area[i][j] == ".":
        area[i][j] = "#"
        if isloop(area):
          sum.add((i, j))
        area[i][j] = "."
  return len(sum)


def isloop(matrix):
  area = copy.deepcopy(matrix)

  i, j = find_guard(data)

  rows = len(area)
  cols = len(area[0])

  directs = [[[] for _ in range(cols)] for _ in range(rows)]


  direction = 0 #0 for up, 1 for right, 2 for down, 3 for left
  sum = 0

  try_i, try_j = next_step(i, j, direction)
  while 0<= try_i < rows and 0 <= try_j < cols:
    if (area[try_i][try_j] == '.') or (area[try_i][try_j] == 'X') or (area[try_i][try_j] == '^') :
      
      i = try_i
      j = try_j
      if area[i][j] == 'X':
        if direction in directs[i][j]:
          return True
      directs[i][j].append(direction)
      area[i][j] = "X"
      
    else:
      direction = (direction + 1) % 4
    try_i, try_j = next_step(i, j, direction)
  
  return False



print(brute_force(data))



