def solution(dirs):
    cur = [5, 5] # 시작 위치는 (5,5)
    cnt = 0 # 중복되지 않게 지나간길 체크 cnt변수 생성
    visited = [] # 방문했던 길 ([],[]) 형식으로 저장

    for i in dirs: # dirs 변수 for문 시작
        if i == 'U': # U이면
            if cur[1] + 1 >= 11: # y축이 범위 11을 넘으면 continue
                continue
            else: # 만약 넘지 않으면
                temp = (cur, [cur[0], cur[1] + 1])  # temp변수 -> A->B지점으로 간 길
                temp2 = ([cur[0],cur[1] + 1], cur) # temp2변수 -> temp1의 반대 B->A로 간 길
                cur = [cur[0], cur[1] + 1] # cur의 값을 수정
            if temp not in visited: # 만약 temp가 방문했던 경로이면
                cnt += 1 # cnt += 1
                visited.append(temp) # temp와 temp2를 visited에 넣어준다.
                visited.append(temp2)
        # DLR모두 U와 같은 방법 이므로 설명 생략
        elif i == 'D':
            if -1 >= cur[1] - 1 :
                continue
            else:
                temp = (cur, [cur[0], cur[1] - 1])
                temp2 = ([cur[0], cur[1] - 1],cur)
                cur = [cur[0], cur[1] - 1]
            if temp not in visited:
                cnt += 1
                visited.append(temp)
                visited.append(temp2)
        elif i == 'L':
            if -1 >= cur[0] - 1:
                continue
            else:
                temp = (cur, [cur[0] - 1, cur[1]])
                temp2 = ([cur[0] - 1, cur[1]],cur)
                cur = [cur[0] - 1, cur[1]]
            if temp not in visited:
                cnt += 1
                visited.append(temp)
                visited.append(temp2)
        elif i == 'R':
            if cur[0] + 1 >= 11:
                continue
            else:
                temp = (cur, [cur[0] + 1, cur[1]])
                temp2 = ([cur[0] + 1, cur[1]], cur)
                cur = [cur[0] + 1, cur[1]]
            if temp not in visited:
                cnt += 1
                visited.append(temp)
                visited.append(temp2)

    return cnt


