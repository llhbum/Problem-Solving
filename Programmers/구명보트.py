#답
def solution(people, limit):
    people.sort()
    answer = 0
    i = 0
    j = len(people) - 1

    while i <= j:
        answer += 1
        if people[j] + people[i] <= limit:
            i += 1
        j -= 1
    return answer
# 오답
def solution(people, limit):
    people.sort(reverse = True)
    answer = 0
    while True:
        if not people:
            break
        else:
            target = people.pop(0)
            for i in range(len(people)):
                if target + people[i] <= limit:
                    answer += 1
                    people.pop(i)
                elif i == len(people) - 1:
                    answer += 1
                    break
    return answer



