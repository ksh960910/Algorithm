def solution(n):
    answer = 0
    tri = list()
    num = n
    while n/3!=0:
        if int(num) == 0:
            break
        tri.append(int(num%3))
        num = int(num)/3
    for i in range(len(tri)):
        answer= answer+ tri[i]*(3**(len(tri)-i-1))
    return answer