def solution(s):
    result = []
    s = list(s)
    for i in s:
        if i == '(':
            result.append(i)
        else:
            try:
                result.pop()
            except:
                return False
    if len(result) == 0:
        return True
    else:
        return False
