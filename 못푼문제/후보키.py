from itertools import combinations
def solution(relation):
    count = 0
    key = [i for i in range(len(relation[0]))]
    for i in range(1,len(key)):
        for j in list(combinations(key,i)):
            if uniqueness(list(j),relation):
                count += 1
    return count
def uniqueness(arr,relation):
    for i in range(len(arr)):
        tmp = []
        for j in range(len(relation)):
            element = []
            for k in arr:
                element.append(relation[j][k])
            tmp.append(element)
        if len(tmp) == len(set(list(map(tuple,tmp)))):
    return False
def minimality(arr):
    if len(arr[0]) == 1:
        return True
    print(arr)
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
