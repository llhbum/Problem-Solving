check = True
while check:
    N,M = map(int,input().split())

    if N == 0 and M == 0:
        check = False
    else:
        print(N+M)

