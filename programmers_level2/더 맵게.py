import heapq

# heapq는 pop, push등을 할때마다 힙을 정렬해준다 / 최소최대 값 구할때 유용

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        num = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, num)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer
