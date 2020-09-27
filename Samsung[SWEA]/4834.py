
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T+1):
#
#     n = int(input())
#     print('이상해')
#     Data = input()
#     Data = [int(_) for _ in Data]
#     n_list = [0] * 10
#
#     for i in range(n):
#         n_list[Data[i]] += 1
#     maxnum = 0
#     maxindex = 0
#
#
#     for i in range(len(n_list)):
#         if maxnum <= n_list[i]:
#             maxnum = n_list[i]
#             maxindex = i
#     print(f'# {test_case} {maxindex} {maxnum}')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 쓰이지 않음
    num_list = list(map(int, input()))

    max_num = -1
    max_cnt = 0
    for i in range(10):
        if num_list.count(i) >= max_cnt:
            max_cnt = num_list.count(i)
            max_num = i

    print('#{} {} {}'.format(test_case, max_num, max_cnt))



