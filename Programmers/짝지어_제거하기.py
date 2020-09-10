def solution(s):
    answer = [] #스택을 만들어준다.
    s = list(s) #s를 list를 변환한다.

    for i in range(len(s)): # s의 길이만큼 for문을 돈다.
        if len(answer) == 0: # 스택에 value가 존재하지 않으면 s[i]를 넣어준다.
            answer.append(s[i])
        else: # 스택에 value가 존재하면
            if s[i] == answer[-1]: # s[i]와 스택[-1](스택의 맨 위에 있는 값)이 같은지 비교한다.
                answer.pop() #같다면 빼네준다.
            else: # 만약 같지 않다면
                answer.append(s[i]) # 스택에 s[i]를 넣어준다.
    # 모든 비교후
    if len(answer) == 0: # 스택에 value가 없다면
        return 1 # 1을 리턴한다.
    else: # 만약 value가 있다면
        return 0 # 0을 리턴한다.