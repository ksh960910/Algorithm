def solution(priorities, location):
    cnt = 0
    while True:
        max_num = max(priorities)
        for i in range(len(priorities)):
            if max_num == priorities[i]:
                cnt+=1
                priorities[i] = 0
                max_num = max(priorities)
                if i == location:
                    return cnt