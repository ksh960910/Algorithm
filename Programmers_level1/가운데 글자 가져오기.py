def solution(s):
    answer = 0
    half = len(s)%2
    if half==1:
        answer = s[int(len(s)/2)]
    else:
        answer = s[int(len(s)/2)-1]+s[int(len(s)/2)]
    return answer