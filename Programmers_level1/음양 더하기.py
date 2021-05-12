def solution(absolutes, signs):
    answer = 0
    for tup in zip(absolutes, signs):
        tup = list(tup)
        if tup[1] == False:
            tup[0]*=-1
        answer+=tup[0]
    return answer