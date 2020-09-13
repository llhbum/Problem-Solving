def solution(priorities, location):
    answer = 0
    while len(priorities) != 0: # priorities의 길이가 0이 아니면
        if priorities[0] == max(priorities): #priorities의 [0]과 priorities의 max 값을 비교해서 같으면
            answer += 1 # answer에 +1을 해준다
            priorities.pop(0) # 그후 priorities의 [0] 값을 pop해준다.

            if location == 0: # location의 값이 0 이면
                return answer # answer을 return 해준다.
            else: #location의 값이 0이 아니면 검사가 끝난게 아니므로
                location -= 1 #location의 값을 -1해주고 while문을 계속 실행 한다.
        else: # priorities의 [0]값이 max 값과 다르면
            priorities.append(priorities.pop(0)) #priorities의 [0] 값을 pop하여 맨 끝에 append한다.
            if location == 0: #만약 location의 값이 0이면
                location = len(priorities) - 1 #location의 값을 priorities의 길이 -1을 해준다.
            else: # location의 값이 0이 아니면
                location -= 1 #location 값을 -1해준다.
    return answer