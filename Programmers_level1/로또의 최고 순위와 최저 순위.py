def solution(lottos, win_nums):
    answer = []
    max_cnt = 0
    min_cnt = 0
    for i in lottos:
        if i in win_nums:
            max_cnt += 1
            min_cnt += 1
        elif i == 0:
            max_cnt += 1
    if max_cnt == 0 or max_cnt == 1:
        answer.append(6)
    elif max_cnt == 2:
        answer.append(5)
    elif max_cnt == 3:
        answer.append(4)
    elif max_cnt == 4:
        answer.append(3)
    elif max_cnt == 5:
        answer.append(2)
    elif max_cnt == 6:
        answer.append(1)

    if min_cnt == 0 or min_cnt == 1:
        answer.append(6)
    elif min_cnt == 2:
        answer.append(5)
    elif min_cnt == 3:
        answer.append(4)
    elif min_cnt == 4:
        answer.append(3)
    elif min_cnt == 5:
        answer.append(2)
    elif min_cnt == 6:
        answer.append(1)

    answer.sort()

    return answer