import itertools
def solution(nums):
    answer = 0
    coms = itertools.combinations(nums, 3)
    for com in coms:
        num = sum(com)
        for i in range(2,num):
            if num%i==0:
                break
        else:
            answer+=1
    return answer