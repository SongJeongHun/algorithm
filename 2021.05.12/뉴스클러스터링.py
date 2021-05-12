"""2h"""
def solution(str1, str2):
    answer = 0
    str1_set = []
    str2_set = []
    j = 0
    while(j != len(str1)):
        target = str1[j:j + 2]
        if target[0].isalpha() and target[1].isalpha():
            str1_set.append(target.lower())
        j += 1
        if(len(str1) - 1 == j):
            break
    j = 0
    while(j != len(str2)):
        target = str2[j:j + 2]
        if target[0].isalpha() and target[1].isalpha():
            str2_set.append(target.lower())
        j += 1
        if(len(str2) - 1 == j):
            break
    union_set,intersection_set = unionAndIntersection(str1_set,str2_set)
    if len(union_set) == 0:
        return 65536
    return int((len(intersection_set) / len(union_set)) * 65536)
def unionAndIntersection(str1,str2):
    union = []
    intersection = []
    result_dict = dict()
    for i in str1:
        if i in result_dict.keys():
            result_dict[i][0] += 1
        else:
            result_dict[i] = [1,0]
    for i in str2:
        if i in result_dict.keys():
            result_dict[i][1] += 1
        else:
            result_dict[i] = [0,1]
    for k,v in result_dict.items():
        if v[0] >= 1 and v[1] >= 1:
            if v[0] <= v[1]:
                for _ in range(v[0]):
                    intersection.append(k)
            else:
                for _ in range(v[1]):
                    intersection.append(k)
        if v[0] >= v[1]:
            for _ in range(v[0]):
                union.append(k)
        else:
            for _ in range(v[1]):
                union.append(k)
    return union,intersection
print(solution('abcccc','cccdefff'))
