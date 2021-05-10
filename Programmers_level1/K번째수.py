def solution(array, commands):
    answer = list()
    for command in commands:
        sorted_array = array[command[0]-1:command[1]]
        sorted_array.sort()
        answer.append(sorted_array[command[2]-1])
    return answer