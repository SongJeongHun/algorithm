def solution(msg):
    answer = []
    start = 65
    table = {chr(start + i):i + 1 for i in range(26)}
    target = ''
    while len(msg) != 0:
        print(answer)
        max_len = max(set(map(lambda x:len(x),table.keys())))
        target = msg[:max_len]
        while True:
            if target in table.keys():
                answer.append(table[target])
                msg = msg[len(target):]
                break
            else:
                max_len -= 1
                target = msg[:max_len]
        if len(msg) != 0:
            target += msg[0]
        table[target] = len(table) + 1
    return answer
print(solution("KAKAO"))
