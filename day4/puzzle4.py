
matrix = []

with open('/Users/student/cs/advent_of_code/day4/data.txt') as file:
  for line in file:
    
    row = [x for x in line.strip()]
    matrix.append(row)

print(len(matrix), len(matrix[0]))
sumhor = 0
sumvert = 0
sumdiag = 0
for i, row in enumerate(matrix):
  for j, val in enumerate(row):
    if val == 'X':
      #search horizontal rightwards
      if j+3 < len(matrix):
        
        if matrix[i][j+1] == 'M' and matrix[i][j+2] == 'A' and matrix[i][j+3] == 'S':
          sumhor += 1
      #search vertical downwards
      if i+3 < len(matrix[0]):
        if matrix[i+1][j] == 'M' and matrix[i+2][j] == 'A' and matrix[i+3][j] == 'S':
          sumvert += 1
      #search diagonla down right
      if i+3 < len(matrix[0]) and j+3 < len(matrix):
        if matrix[i+1][j+1] == 'M' and matrix[i+2][j+2] == 'A' and matrix[i+3][j+3] == 'S':
          sumdiag += 1
      #search diagonal down left
      if i-3 >= 0 and j+3 < len(matrix):
        if matrix[i-1][j+1] == 'M' and matrix[i-2][j+2] == 'A' and matrix[i-3][j+3] == 'S':
          sumdiag += 1
    elif val == "S":
      #search horizontal rightwards
      if j+3 < len(matrix):
        if matrix[i][j+1] == 'A' and matrix[i][j+2] == 'M' and matrix[i][j+3] == 'X':
          sumhor += 1
      #search vertical downwards
      if i+3 < len(matrix[0]):
        if matrix[i+1][j] == 'A' and matrix[i+2][j] == 'M' and matrix[i+3][j] == 'X':
          sumvert += 1
      #search diagonla down right
      if i+3 < len(matrix[0]) and j+3 < len(matrix):
        if matrix[i+1][j+1] == 'A' and matrix[i+2][j+2] == 'M' and matrix[i+3][j+3] == 'X':
          sumdiag += 1
      #search diagonal down left
      if i-3 >= 0 and j+3 < len(matrix):
        if matrix[i-1][j+1] == 'A' and matrix[i-2][j+2] == 'M' and matrix[i-3][j+3] == 'X':
          sumdiag += 1

print("horizonal", sumhor)
print("vertical", sumvert)
print("diagonal", sumdiag)
print("total", sumdiag+sumhor+sumvert)