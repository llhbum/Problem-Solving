N = (int(input()))

M = input()
M_int = int(M)
M_list = list(map(int,M))

result =[]

for i in M_list:

    temp = N * i
    # print(temp)
    result.append(temp)
result.reverse()
# print(result)
for j in result:
    print(j)
print(M_int*N)