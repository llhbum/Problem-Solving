N_list = []
for i in range(5):
    temp = int(input())
    if temp < 40:
        temp = 40
        N_list.append(temp)
    else:
        N_list.append(temp)
result  = int(sum(N_list)/5)

print(result)
