# 정답
def solution(answers):
    answer = [0, 0, 0]
    result = []
    answer_1 = [1, 2, 3, 4, 5]
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == answer_1[i % len(answer_1)]: answer[0] += 1
        if answers[i] == answer_2[i % len(answer_2)]: answer[1] += 1
        if answers[i] == answer_3[i % len(answer_3)]: answer[2] += 1

    max_ans = max(answer)
    for i in range(len(answer)):
        if max_ans == answer[i]:
            result.append(i + 1)
    return result

# 풀이
def solution(answers):
    answer = [0, 0, 0] # 1,2,3 수포자의 답 개수
    result = [] # 마지막 결과 리스트
    answer_1 = [1, 2, 3, 4, 5] #수포자1의 정답 패턴
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5] #수포자2의 정답 패턴
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #수포자3의 정답 패턴

    for i in range(len(answers)): # 주어진 정답 만큼 for문을 돌림
        if answers[i] == answer_1[i % len(answer_1)]: answer[0] += 1 # 주어진 정답과 일치하면 answer[0]에 +1 해준다.
        if answers[i] == answer_2[i % len(answer_2)]: answer[1] += 1 # 수포자들의 정답 패턴 보다 더 긴 정답이 요구될 수 있기 때문에
        if answers[i] == answer_3[i % len(answer_3)]: answer[2] += 1 # %(나머지 연산자)를 이용해서 조건을 만족 시켜준다.

    max_ans = max(answer) # answer중 max값을 찾고
    for i in range(len(answer)): # for 문을 돌려
        if max_ans == answer[i]: # max값과 answer[i]값이 같으면
            result.append(i + 1) # result에 n번 수포자를 넣어준다.
    return result