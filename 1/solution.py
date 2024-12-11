f = open("input.txt")
array1 = []
array2 = []
diff = 0
diff2 = 0
for line in f:
    line = line.strip()
    data = line.split()
    array1.append(int(data[0]))
    array2.append(int(data[1]))

array1.sort()
array2.sort()
for i in range(len(array1)):
    diff += abs(array1[i] - array2[i])
# print(array1)
# print(array2)

print(diff)

# Part 2 - calculate diff2
for i in array1:
    #print(i)
    diff2 += i * array2.count(i)
print(diff2)