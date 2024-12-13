import copy

def readFile (file):
    fileMap = [[] for i in range(1000)]
    i = 0
    with open(file, 'r') as file:
        for line in file:
            lineList = line.strip().split()
            lineListInt = [int(item)for item in lineList]
            fileMap[i]=lineListInt
            i+=1
    return fileMap

# def isSorted (array):
#     if (sorted(array) == array) or (sorted(array, reverse=True) == array):
#         return True
#     else:
#         return False

# means that difference is between 0 and 3
def isSafe (array):
    for i in range(len(array)-1):
        if (abs(array[i] - array[i+1]) > 3) or (abs(array[i] - array[i+1]) == 0):
            return False
    if (sorted(array) == array) or (sorted(array, reverse=True) == array):
        return True
    else:
        return False 

def hasDoubles (array):
    for i in range(len(array)-1):
      if (abs(array[i] - array[i+1]) == 0):
        return True
      else:
        return False

def removeDoubles (array):
    for i in range(len(array)-1):
      if (abs(array[i] - array[i+1]) == 0):
        del array[i]
        return array

input = readFile('day2.txt')
input2 = []

safeCounter = 0
errorCounter = 0
for line in input:
    if isSafe(line):
        #print(line)
        safeCounter +=1
    else:
        input2.append(line)
print("Solution exercise1 (safe lines): ", safeCounter)



for line in input2:
    # print(line)
    # i+=1
    # print(i)
    shortedLine=copy.copy(line)
    goodToGo = True
    for i in range(len(line)):
        if goodToGo:
            
            del shortedLine[i]
            
            if isSafe(shortedLine):
                safeCounter +=1
                goodToGo = False
            else:
                shortedLine=copy.copy(line)

print("Solution including one allowed error: ",safeCounter)

    