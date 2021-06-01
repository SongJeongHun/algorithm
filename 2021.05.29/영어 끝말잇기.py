def solution(n, words):
    answer = []
    count = 0
    for i in range(len(words)):
        if (i) % n == 0:
            count += 1
        answer.append(words[i])
        if answer.count(words[i]) > 1:
            return [(i % n) + 1,count]
        if words[i - 1][-1] != words[i][0] and i != 0:
            return [(i % n) + 1,count]
    return [0,0]
