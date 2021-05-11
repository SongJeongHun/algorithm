def solution(n, lost, reserve):
    count = n
    time = 0
    for i in lost.copy():
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
            time += 1
    if len(lost) == 0 and len(reserve) == 0:
        return n - time
    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            reserve.remove(i + 1)
        else:
            count -= 1
    return count
print(solution(5,[2,1],[1,2]))
