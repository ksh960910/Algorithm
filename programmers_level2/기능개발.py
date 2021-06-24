import math


def solution(progresses, speeds):
    day = []
    answer = []
    front = 0
    for i in range(len(progresses)):
        release = math.ceil((100 - progresses[i]) / speeds[i])
        day.append(release)
    for idx in range(len(day)):
        if day[idx] > day[front]:
            answer.append(idx - front)
            front = idx
    answer.append(len(day) - front)
    return answer