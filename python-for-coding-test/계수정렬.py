array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
set_array = set(array)
cntList = [0 for _ in range(len(set_array))]
for i in range(len(array)):
    cntList[array[i]] += 1

resultList = []
for i in range(len(cntList)):
    for j in range(cntList[i]):
        resultList.append(i)
print(resultList)