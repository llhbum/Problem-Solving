def solution(array, commands):
    answer = []
    for i in commands:
        temp_list = array[i[0]-1 : i[1]]
        temp_list.sort()
        answer.append(temp_list[i[2] - 1])
    return answer

