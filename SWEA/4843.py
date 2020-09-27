'''
1. 수를 입력받고
2. 입력받은 수를 정렬한다.
3. len/2해서 각각 리스트에 append한다.
4. 각 리스트를 하나씩 차례대로 출력한다.

123 3개 면 len = 3/2 = 1 [3]len/2까지 [1,2]len/2)+1까지
312
'''



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()

    half_len = int(len(n_list) / 2)

    high_list = []
    low_list = []
    for i in range(n):
        if i < half_len:
            low_list.append(n_list[i])
        else:
            high_list.append(n_list[i])

    # print(low_list)
    high_list.sort(reverse=True)
    # print(high_list)
    '''
    [8, 11, 16, 28, 39]
    [89, 85, 67, 60, 49]
    '''
    result = []
    for i in range(len(low_list)):
        result.append(high_list[i])
        result.append(low_list[i])
    result.append(high_list[len(high_list) - 1])

    result_str = ' '.join(map(str, result[0:10]))

    print(f'#{test_case} {result_str}')




