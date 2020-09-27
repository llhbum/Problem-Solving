# """
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 Progresses와
# 작업의 개발 속도가 적힌 정수 배열 speeds가
# 주어질 때 각 배포마다 몇개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하라
#
# """
#
import math

pro = [95, 90, 99, 99, 80, 99]
sp = [1, 1, 1, 1, 1, 1]
# # pro = [95, 90, 99, 99, 80, 99]
# # sp = [1, 1, 1, 1, 1, 1]
#


def finish_time(progresses, speeds):
    finish = []
    for i in range(len(progresses)):
        temp = (100 - progresses[i])
        temp2 = temp // speeds[i]
        if temp % speeds[i] != 0:
            temp2 += 1
        finish.append(temp2)
    return finish


def return_time(finish):
    answer = []
    front = 0
    for idx in range(len(finish)):
        if finish[idx] > finish[front]:
            answer.append(idx - front)
            front = idx
    answer.append(len(finish) - front)
    return answer

def solution(progresses, speeds):
    finish = finish_time(progresses, speeds)
    answer = return_time(finish)
    return answer




def finish_time(progresses, speeds):
    finish = []
    for i in range(len(progresses)):
        temp = (100 - progresses[i])
        temp2 = temp // speeds[i]
        if temp % speeds[i] != 0:
            temp2 += 1
        finish.append(temp2)
    return finish

def return_time(finish):
    answer = []
    std = finish.pop(0)
    while True:
        cnt = 1
        if len(finish) == 0:
            break
        else:
            for i in finish:
                if std < i:
                    std = i
                    for _ in range(cnt):
                        finish.pop(0)
                    answer.append(cnt)
                    if len(finish) == 0:
                        answer.append(1)
                        break
                    break
                else:
                    cnt += 1
                    if len(finish) == 1:
                        finish.pop(0)
                        answer.append(cnt)
                        break
    return answer

def solution(progresses, speeds):
    finish = finish_time(progresses, speeds)
    answer = return_time(finish)
    return answer

