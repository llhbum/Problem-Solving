N = int(input())
CNT = 0
while True:
    if N % 5 == 0:
        CNT = CNT + (N//5)
        print(CNT)
        break
    N = N - 3
    CNT += 1
    if N < 0:
        print(-1)
        break