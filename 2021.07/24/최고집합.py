def solution(n, s):
    answer = []
    mid = s // n
    rest = s % n
    if mid == 0:
        return [-1]
    for i in range(n - rest):
        answer.append(mid)
    for i in range(rest):
        answer.append(mid + 1)
    return answer
