def solution(num):
    cnt = 0
    div = num
    for i in range(500):
        if div==1:
            return cnt
        if div%2==0:
            div/=2
            cnt+=1
        else:
            div = div*3 + 1
            cnt+=1
    if cnt==500 and div!=1:
        return -1
    return cnt