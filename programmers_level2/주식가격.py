from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        price = queue.popleft()
        cnt = 0
        for i in queue:
            cnt+=1
            if price > i:
                break
        answer.append(cnt)
    return answer
