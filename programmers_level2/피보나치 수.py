def solution(n):
    pibo = [0,1]
    for i in range(2,n+1):
        pibo.append(pibo[i-2]+pibo[i-1])
    return pibo[n]%1234567