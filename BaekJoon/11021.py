import sys

N = int(input())
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    result = A + B

    print(f'Case #{i+1}: {result}')
