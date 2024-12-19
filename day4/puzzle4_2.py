matrix = []

with open('/Users/student/cs/advent_of_code/day4/data.txt') as file:
  for line in file:
    
    row = [x for x in line.strip()]
    matrix.append(row)



def is_downright(matrix, i, j, par):
  if par == 'M':
    if i+2 < len(matrix[0]) and j+2 < len(matrix):
      if matrix[i+1][j+1] == 'A' and matrix[i+2][j+2] == 'S':
        return True
  elif par == 'S':
    if i+2 < len(matrix[0]) and j+2 < len(matrix):
      if matrix[i+1][j+1] == 'A' and matrix[i+2][j+2] == 'M':
        return True
  return False

def is_downleft(matrix, i, j, par):
  if par == 'M':
    if i+2 < len(matrix[0]) and j-2 >= 0:
      if matrix[i+1][j-1] == 'A' and matrix[i+2][j-2] == 'S':
        return True
  elif par == 'S':
    if i+2 < len(matrix[0]) and j-2 < len(matrix):
      if matrix[i+1][j-1] == 'A' and matrix[i+2][j-2] == 'M':
        return True
  return False


sum = 0
for i, row in enumerate(matrix):
  for j, val in enumerate(row):
    if is_downright(matrix, i, j, val) and is_downleft(matrix, i, j+2, matrix[i][j+2]):
      sum += 1

print(sum)