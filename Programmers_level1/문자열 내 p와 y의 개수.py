def solution(s):
    answer = True
    s = s.lower()
    cnt_p = 0
    cnt_y = 0
    for i in s:
        if i=='p':
            cnt_p+=1
        elif i=='y':
            cnt_y+=1
    if cnt_p==cnt_y:
        answer = True
    else:
        answer = False
    return answer