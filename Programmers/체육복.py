
# 오답
def solution(n, lost, reserve):
    answer = 0
    temp = []
    for i in lost:
        for j in reserve:
            if i >= 2:
                if i == j - 1 or i == j + 1:
                    temp.append(i)
                    reserve.pop(0)
                    break
            else:
                if i == j + 1:
                    temp.append(i)
                    reserve.pop(0)
                    break
    temp_n = len(set(temp))
    temp_n = len(lost) - temp_n
    answer = n - temp_n
    return answer

# 답

def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)
