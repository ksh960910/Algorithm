def solution(s):
    answer = True
    if len(s)==4 or len(s)==6:
        try:
            s = int(s)+1
            answer = True
        except:
            answer= False
    else:
        answer = False
    return answer