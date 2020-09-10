
def solution(s):
    answer = []
    s = list(s)

    for i in range(len(s)):
        if len(answer) == 0:
            answer.append(s[i])
        else:
            if s[i] == answer[-1]:
                answer.pop()
            else:
                answer.append(s[i])
    if len(answer) == 0:
        return 1
    else:
        return 0








