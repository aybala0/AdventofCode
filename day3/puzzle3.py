

#returns 0 if not num, returns the length of the num if is num
def isnum(str, i):
  if 48 <= ord(str[i]) <= 57:
    return 1 + isnum(str, i+1)
  else:
    return 0

  

sum = 0
with open('/Users/student/cs/advent_of_code/day3/data1.txt') as file:
  do = True
  for line in file:
    for i, _ in enumerate(line):
      if(line[i: i+2] == "do"):
        if(line[i+2: i+4] == "()"):
          do = True
        elif(line[i+2: i+7] == "n't()"):
          do = False
      if do:
        if(line[i:i+3] == "mul") and line[i + 3] == "(":

          total = isnum(line, i + 4)
          if total != 0:

            if line[i + total + 4] == ",":
              total2 = isnum(line, i + total + 5)
              if total2 != 0:
                if line[i + total + 5 + total2] == ")":
      
                  mult = int(line[i + 4: i + 4 + total]) * int(line[ i + total + 5 : i + total + 5+ total2])

                  sum+= mult


print(sum)