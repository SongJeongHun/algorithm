def solution(s):
    answer = []
    s = s[1:-1]
    if '},{' in s:
        s = list(s.split('},{'))
    else:
        s = int(s[1:-1])
        answer.append(s)
        return answer
    s = sorted(s,key = lambda x: x.count(','))
    for i in s:
        tmp = ''
        if '}' in i:
            tmp = i.replace('}','')
            tmp = list(map(int,tmp.split(',')))
            for j in tmp:
                if not j in answer:
                    answer.append(j)
        elif '{' in i:
            tmp = i.replace('{','')
            tmp = list(map(int,tmp.split(',')))
            for j in tmp:
                if not j in answer:
                    answer.append(j)
        elif len(i) == 1:
            if not int(i) in answer:
                answer.append(int(i))
        else:
            tmp = list(map(int,i.split(',')))
            for j in tmp:
                if not j in answer:
                    answer.append(j)
    return answer
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
