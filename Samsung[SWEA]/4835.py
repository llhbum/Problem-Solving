
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, (input().split()))

    # N = 총개수
    # M = 인접한 수의 개수

    n_list = list(map(int, input().split()))
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Max_sum = Min_sum = sum(n_list[0:M])

    for i in range(N-M+1):
        temp_sum = 0
        temp_sum = sum(n_list[i:M+i])
        if temp_sum>Max_sum:
            Max_sum = temp_sum
        elif temp_sum<Min_sum:
            Min_sum = temp_sum
    print(f'#{test_case} {Max_sum - Min_sum}')



