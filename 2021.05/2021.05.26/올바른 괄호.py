def solution(s):
    answer = []    
    for i in s:
        if i == '(':
            answer.append('(')
        else:
            if len(answer) == 0:
                return False
            answer.pop()
    print(answer)
    if len(answer) == 0:
        return True
    else:
        False
print(solution("(()("))
