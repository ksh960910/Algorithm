def solution(arr, divisor):
    answer = list()
    for i in arr:
        if i%divisor==0:
            answer.append(i)
    if len(answer)==0:
        answer.append(-1)
    return sorted(answer)