def solution(s):
    n = list(map(int,s.split(' ')))
    answer = str(min(n)) + " " + str(max(n))
    return answer
