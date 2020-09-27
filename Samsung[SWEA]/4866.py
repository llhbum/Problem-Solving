
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    stack = []
    result = 1
    str_list = list(input())
    for i in range(len(str_list)):
        if str_list[i] == '{' or str_list[i] == '(':
            stack.append(str_list[i])
        if str_list[i] == '}' or str_list[i] == ')':
            if not stack:
                result = 0
                break
            temp = stack.pop()
            if str_list[i] == ')' and temp != '(':
                result = 0
            if str_list[i] == '}' and temp != '{':
                result = 0


    if stack:
        result = 0

    print(f'#{test_case} {result}')




