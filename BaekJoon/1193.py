N = int(input())
cnt=1
while True:
    if N>cnt:
        N = N - cnt
        cnt += 1
    else:
        break
if cnt % 2 == 0:
    print(f'{N}/{cnt - (N - 1)}')
else:
    print(f'{cnt - (N - 1)}/{N}')


