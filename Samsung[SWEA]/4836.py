


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    palette = [[0 for _ in range(10)] for _ in range(10)]
    result = 0
    n = int(input())

    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if color == 1:
                    if palette[r][c] == 0:
                        palette[r][c] = 1
                    elif palette[r][c] == 2:
                        palette[r][c] = 3
                        result += 1
                elif color == 2:
                    if palette[r][c] == 0:
                        palette[r][c] = 2
                    elif palette[r][c] == 1:
                        palette[r][c] = 3
                        result += 1
    print(f'#{test_case} {result}')






