
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    nums = [i for i in range(1, N + 1)]

    lst = []
    for i in range(1 << len(nums)):
        sub_lst = []
        for j in range(len(nums)):
            if i & (1 << j):
                sub_lst.append(nums[j])
        lst.append(sub_lst)
    # print(lst)

    result = 0
    for i in range(len(lst)):
        if sum(lst[i]) == K and len(lst[i]) == N:
            result += 1
            # print(sum(lst[i]), len(lst[i]))
    print(f'#{test_case} {result}')