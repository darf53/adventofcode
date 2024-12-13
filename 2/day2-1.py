f = open("day2.txt", "r")
# print(f.readline())

safeCount = 0
safe = True
issues = 0

with open('day2.txt', 'r') as file:
  for line in file:
    lineList = line.strip().split()
    lineListInt = [int(item)for item in lineList]
    for i in range(len(lineListInt)-1):
      if (abs(lineListInt[i] - lineListInt[i+1]) > 3) or (abs(lineListInt[i] - lineListInt[i+1]) == 0):
        safe = False
        #print(safe)
        break

    if safe:
      if (sorted(lineListInt) == lineListInt) or (sorted(lineListInt, reverse=True) == lineListInt):
        safeCount +=1
        # print(safe)
        # print(lineListInt)
      else: 
        safe = False
        #print("not sorted", lineListInt)
        print(line.strip())
    else:
      print(line.strip())
      #print("jump too much ", lineListInt)
      safe = True
print(safeCount)



# or (sorted(lineListInt, reverse=True) != lineListInt)

# test = ['71', '72', '75', '76', '78']
# print(test)
# print(sorted(test))
# print(sorted(test, reverse=True))
# print(test != sorted(test))
# print(test != sorted(test, reverse=True))