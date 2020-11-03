'''
N이 1일 될 때까지 두 과정중 하나를 반복
단, 두번째 연산은 N이 K로 나누어떨어질 때만 선택
1. N에서 1을 뺸다
2. N을 K로 나눈다.
'''

"""
INPUT
25 5

17 4
"""

n, k  = map(int,input().split())
result = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n = n / k
        result += 1
    else:
        n -= 1
        result += 1




print(result)