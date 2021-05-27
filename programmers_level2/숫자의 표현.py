def solution(n):
    answer = 0
    for i in range(1, n + 1):
        agg = 0
        for j in range(i, n + 1):
            agg += j
            if agg == n:
                answer += 1
                break
            elif agg > n:
                break
    return answer
