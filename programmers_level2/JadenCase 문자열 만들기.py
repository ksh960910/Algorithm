def solution(s):
    answer = ''
    temp = s.split(' ')
    for i in temp:
        if i == '':
            answer += ' '
        else:
            answer += i[0].upper() + i[1:].lower() if len(i) > 1 else i.upper()
            answer += ' '

    answer = answer[:-1]
    return answer