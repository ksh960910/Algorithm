''' https://programmers.co.kr/learn/courses/30/lessons/42583 

bridge_length	weight	truck_weights	                return
2	              10	 [7,4,5,6]	                      8
100	              100	    [10]	                     101
100	              100	[10,10,10,10,10,10,10,10,10,10]	 110

'''

def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge = [0] * bridge_length
    while on_bridge:
        time+=1
        on_bridge.pop(0)
        if truck_weights:
            if sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights.pop(0))
            else:
                on_bridge.append(0)
    return time