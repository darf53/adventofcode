f = open("day2.txt", "r")
print(f.readline())

safeCount = 0
safe = True

with open('day2.txt', 'r') as file:
  for line in file:
    lineList = line.strip().split()
    lineListInt = [int(item)for item in lineList]
    for i in range(len(lineList)-1):
      if abs(lineListInt[i] - lineListInt[i+1]) >2:
        safe = False
        print(safe)
        break
    if safe:
      safeCount +=1
      print(safe)
    else:
      safe = True
    print(lineList)
print(safeCount)



