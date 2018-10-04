num = int(input())
count = 1
myList = []
for i in range(num):
    myList.append([])
    for j in range(num):
        myList[i].append(count)
        count += 1
for i in range(0, 1):
    for j in range(0, num):
        myList[i][j] = count
        count += 1
for i in range(1, num):
    myList[i][num - 1] = count
    count += 1
print(myList)
for j in range(2, num + 1):
    myList[num - 1][num - j] = count
    count += 1
print(myList)
for i in range(2, num):
    myList[num - i][0] = count
    count += 1
print(myList)
for j in range(1, num - 1):
    myList[0 + 1][0 + j] = count
    count += 1
print(myList)
for i in range(2, num - 1):
    myList[i][num - 2] = count
    count += 1
for j in range(3, num):
    myList[num - 2][num - j] = count
    count += 1
for i in range(0, num):
    for j in range(0, num):
        print(myList[i][j], end=' ')
    print('\t')
