def solution(n, a, b):
    cnt = 0
    while a!=b:
        a, b = (a+1)//2, (b+1)//2
        cnt+=1
    return cnt

print(solution(16,4,11))