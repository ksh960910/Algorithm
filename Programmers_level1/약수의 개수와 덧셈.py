def solution(left, right):
    answer = 0
    cnt=0
    for i in range(left,right+1):
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1
        if cnt%2==1:
            i*=-1
        cnt=0
        answer+=i
    return answer