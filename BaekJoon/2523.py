'''
2 * N - 1까지
0 1
1 2
2 3
3 - 1 2
4-  3 1

'''
N = int(input())

a= []
b = []

for i in range(2*N-1):
    if i < N :
        a.append(i+1)
        # print('*'*(i+1))
    else:
        b.append(i-N+1)
        # print('*' * (i-N+1))

b.reverse()
for i in a:
    print('*'*i)
for j in b:
    print('*'*j)
