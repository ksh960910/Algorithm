def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        flag = True
        for i in word:
            if flag==True:
                answer+=i.upper()
                flag = False
            else:
                answer+=i.lower()
                flag = True
        answer+=' '
    return answer[:-1]