def solution(s):
    alpha = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    tmp = ''
    answer = ''
    for i in s:
        if i.isdigit():
            answer += str(i)
        else:
            tmp += i  
        if tmp in alpha.keys():
            answer += str(alpha[tmp])
            tmp = ''
    return answer
print(solution("one4seveneight"))
