def solution(n):
    str_list = list()
    answer = list()
    for i in str(n):
        str_list.append(int(i))
    str_list.sort(reverse=True)
    for j in str_list:
        answer.append(str(j))
    return int(''.join(answer))