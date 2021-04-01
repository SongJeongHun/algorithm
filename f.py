def solution(s):
    answer = 0
    count = 0
    tmp = ""
    new = ""
    for i in s:
        count = 1
        if tmp == i:
            count+=1
            new = s.replace(tmp,str(count)+tmp)
        tmp = i
        
    return new
