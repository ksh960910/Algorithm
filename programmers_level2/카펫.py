def solution(brown, yellow):
    total = brown + yellow
    row, col = 0,0
    coms = []
    for i in range(1, total):
        arr = []
        if total % i == 0:
            arr.append(i)
            arr.append(int(total / i))
            coms.append(arr)
    for com in coms:
        if (com[0]*2 + com[1]*2 - 4) == brown and com[0] >= com[1]:
            return com

