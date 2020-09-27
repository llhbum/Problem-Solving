'''
#
# 문자열s
# r번 반복
# 새문자열 p
# '''
# t = int(input())
# for i in range(t):
#     num,s = input().split()
#     text = ""
#     for i in s:
#         text+=int(num) * i
#     print(text)
n = int(input())


for j in range(n):
    N, s = input().split()
    N = int(N)
    s_list = list(s)
    result = []
    for i in range(len(s_list)):
        for j in range(N):
            result.append(s_list[i])
    print()
    for k in result:
        print(k, end='')