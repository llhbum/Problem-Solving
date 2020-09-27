n = int(input())

for i in range(1,n+1):
    for j in range(n):
        if n-i <= j:
            print('*',end='')
        else:
            print(' ',end='')
    print()
