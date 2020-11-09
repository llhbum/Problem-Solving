'''
02984

567
'''

n = input()
nList = []
for str in n:
    nList.append(int(str))
result = nList[0]

for i in nList[1:]:
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i
print(result)