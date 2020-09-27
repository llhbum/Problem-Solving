s = input()
s_list=list(s)



alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alp_index = [-1 for _ in range(26)]

for i in range(len(s_list)):
    for j in range(len(alp)):
        if alp_index[j] == -1:
            if s_list[i] == alp[j]:
                alp_index[j] = i


for i in alp_index:
    print(i,end=' ')

# [1 0, -1, -1, 2, -1, -1, -1, -1, 4, 3, -1, -1, 7, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1