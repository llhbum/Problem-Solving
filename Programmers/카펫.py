#오답
def solution(brown, yellow):
    answer = []
    sum_c = brown + yellow
    sum_c_2 = sum_c // 2

    for i in range(3, sum_c_2):
        temp = sum_c // i
        if i * temp == sum_c and i >= temp:
            answer.append(i)
            answer.append(sum_c/i)
            return answer

# 답
def solution(brown, red):
    answer = []
    temp = brown + red
    # 가로길이는 세로 길이와 같거나, 세로길이보다 길다.
    sero = 3
    garo = temp // sero

    while (garo >= sero):
        if ((garo - 2) * (sero - 2) == red):
            answer = [garo, sero]
            break
        garo -= 1
        sero = temp // garo
    return answer


