"""
INPUT
5 8 3
2 4 5 4 6

5 7 2
3 4 3 4 3
"""

# N  배열의 크기
# M  숫자가 더해지는 횟수
# K  연속으로 더할 수 있는 수
N, M, K = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort(reverse = True)
# print(numList)
#[6, 5, 4, 4, 2]

cnt = 0
sum = 0

while True:
    for _ in range(K):
        if cnt == M:
            break
        sum += numList[0]
        cnt += 1
    if cnt == M:
        break
    sum += numList[1]
    cnt += 1
print(sum)

