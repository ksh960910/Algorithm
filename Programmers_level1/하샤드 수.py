def solution(x):
    answer = True
    agg = 0
    for i in str(x):
        agg+=int(i)
    if x%agg==0:
        answer = True
    else:
        answer = False
    return answer