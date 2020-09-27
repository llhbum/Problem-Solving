T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n_list = list(input().split())
    stack = []
    flag = 0

    for i in range(len(n_list)-1):
        if n_list[i].isdigit():
            stack.append((n_list[i]))
        else:
            try:
                n2,n1 = int(stack.pop()) , int(stack.pop())
                if n_list[i] == '+':
                    n3 = n1 + n2
                elif n_list[i] == '-':
                    n3 = n1 - n2
                elif n_list[i] == '*':
                    n3 = n1 * n2
                elif n_list[i] == '/':
                    n3 = n1 / n2
                stack.append(str(n3))

            except :
                flag = 987654321

    if flag == 0 and len(stack) == 1:
        print(f'#{test_case} {stack[0]}')

    elif flag == 987654321 or len(stack) > 1:
        print(f'#{test_case} error')
