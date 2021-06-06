def solution(N, stages):
    stages.sort()
    result = {i:0 for i in range(N- 1)}
    answer = {}
    a = []
    for i in stages:
        if i in result.keys():
            result[i] += 1
        else:
            result[i] = 1
    print(result)
    values = list(result.values())
    for v in range(len(values)):
        fail = values[v]
        suc = sum(values[v:])
        if list(result.keys())[v] > N:
            answer[v] = 0
        else:
            answer[v] = fail / suc
    return [i[0] + 1 for i in sorted(answer.items(),key = lambda x:x[1],reverse = True)]
print(solution(4,[4,4,4,4]))
