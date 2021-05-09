def solution(nums):
    pokemon = list()
    N = len(nums) / 2
    for i in nums:
        if i not in pokemon:
            pokemon.append(i)
    if N < len(pokemon):
        answer = N
    else:
        answer = len(pokemon)

    return answer