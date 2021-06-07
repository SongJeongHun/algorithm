import re
def solution(dartResult):
    tmp = dartResult
    answer = []
    n = 0
    num = re.findall('\d+',tmp)
    if len(num[0]) == 2:
        first_index = tmp.index(num[0]) 
        tmp = tmp.replace(num[0],'--',1)
    else:
        first_index = tmp.index(num[0])
        tmp = tmp.replace(num[0],'-',1)
    if len(num[1]) == 2:
        second_index = tmp.index(num[1])
        tmp = tmp.replace(num[1],'--',1)
    else:
        second_index = tmp.index(num[1])
        tmp = tmp.replace(num[1],'-',1)
    if len(num[2]) == 2:
        third_index = tmp.index(num[2])
        tmp = tmp.replace(num[2],'--',1)
    else:
        third_index = tmp.index(num[2])
        tmp = tmp.replace(num[2],'-',1)
    first = dartResult[first_index:second_index]
    second = dartResult[second_index:third_index]
    third = dartResult[third_index:]
    if '*' in first or '#' in first:
        if first[-2] == 'S':
            n = int(first[:-2]) ** 1
        elif first[-2] == 'D':
            n = int(first[:-2]) ** 2
        else:
            n = int(first[:-2]) ** 3
        if first[-1] == '*':
            n *= 2
        elif first[-1] == '#':
            n = -(n)
    else:
        if first[-1] == 'S':
            n = int(first[:-1]) ** 1
        elif first[-1] == 'D':
            n = int(first[:-1]) ** 2
        else:
            n = int(first[:-1]) ** 3
    answer.append(n)
    if '*' in second or '#' in second:
        if second[-2] == 'S':
            n = int(second[:-2]) ** 1
        elif second[-2] == 'D':
            n = int(second[:-2]) ** 2
        else:
            n = int(second[:-2]) ** 3
        if second[-1] == '*':
            answer[0] *= 2
            n *= 2
        elif second[-1] == '#':
            n = -(n)
    else:
        if second[-1] == 'S':
            n = int(second[:-1]) ** 1
        elif second[-1] == 'D':
            n = int(second[:-1]) ** 2
        else:
            n = int(second[:-1]) ** 3
    answer.append(n)
    if '*' in third or '#' in third:
        if third[-2] == 'S':
            n = int(third[:-2]) ** 1
        elif third[-2] == 'D':
            n = int(third[:-2]) ** 2
        else:
            n = int(third[:-2]) ** 3
        if third[-1] == '*':
            answer[1] *= 2
            n *= 2
        elif third[-1] == '#':
            n = -(n)
    else:
        if third[-1] == 'S':
            n = int(third[:-1]) ** 1
        elif first[-1] == 'D':
            n = int(third[:-1]) ** 2
        else:
            n = int(third[:-1]) ** 3
    answer.append(n)
    return sum(answer)
print(solution('10S10T10D'))
