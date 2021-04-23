def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1,int(len(s) / 2) + 1):
        tmp = ''
        cnt = 1
        for j in range(0,len(s),i):
            if s[j:j + i] == s[j + i:j + i + i] :
                cnt += 1
            else:
                if cnt == 1:
                    tmp += s[j:j + i]
                else:
                    tmp += str(cnt) + s[j:j + i]
                cnt = 1
        result.append(len(tmp))
    return min(result)


