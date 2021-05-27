def solution(n):
    answer = n
    while True:
        if bin(n)[2:].count('1')!=bin(answer+1)[2:].count('1'):
            answer+=1
        else:
            return answer+1