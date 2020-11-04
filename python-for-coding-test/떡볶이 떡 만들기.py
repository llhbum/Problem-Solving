'''
INPUT
4 6
19 15 10 17
최소 max 값보다 작아야한다

'''
#오답 문제이해 잘못

# n, m = map(int,input().split())
# nList = list(map(int,input().split()))
# print(nList)
# maxNum = max(nList)
# lenD = 0
# result = 0
# for i in range(maxNum):
#     if m == 0:
#         result = 0
#         break
#     for j in nList:
#         if j-i > 0:
#             lenD += j - i
#     if lenD == m:
#         result = i
#         break
#     else:
#         lenD = 0
# print(result)

# 탐색범위 넓을때 이진탐색

# 정답
n, m = map(int,input().split())
nList = list(map(int,input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(nList)

# 이진 탐색 수행 (반복)
result = 0
while(start <= end):
    total = 0
    mid =  (start + end) // 2
    for x in nList:
        # 양수이면 total에 포함
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)

