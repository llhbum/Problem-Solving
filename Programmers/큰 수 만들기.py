#답
def solution(number, k):
    answer = ""
    stack = []
    number = list(map(int, number))

    for i in range(len(number)):
        stack.append(number[i])

        if len(stack) < 2:
            continue
        else:
            while k > 0 and stack[-1] > stack[-2]:
                stack.pop(-2)
                k -= 1
                if len(stack) == 1:
                    break

    while k > 0:
        stack.remove(min(stack))
        k -= 1

    for i in stack:
        answer += str(i)
    return answer

#풀이
def solution(number, k):
    answer = ""
    stack = [] #스택을 이용한 풀이
    number = list(map(int, number))

    for i in range(len(number)):
        stack.append(number[i])#number에서 가장 앞 수를 stack에 넣어줌

        if len(stack) < 2: #만약 스택의 길이가 2보다 작다면
            continue #다른 원소와 비교할 수 없으므로 continue
        else: #만약 2보다 크거나 같다면
            while k > 0 and stack[-1] > stack[-2]: #k의 수를 검사하고 스택의 맨마지막 수 2개를 비교
                stack.pop(-2) #조건에 부합하다면 맨마지막 수를 pop
                k -= 1 #pop했으므로 k를 -1
                if len(stack) == 1: # 검사 만약 stack의 길이가 1이라면
                    break #종료

    while k > 0: #k가 남았다면
        stack.remove(min(stack)) #stack에서 가장 작은 값 제거
        k -= 1 #k -1

    for i in stack: #stack의 수를 문자열로 만들어
        answer += str(i)
    return answer #제출