alp = list(map(chr,range(65,90)))
num = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]

timeList = []
str = input()
for k in range(len(str)):
    time = 0
    time += num[alp.index(str[k])] + 1
    timeList.append(time)
print(sum(timeList))