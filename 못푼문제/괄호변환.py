def solution(p):
    loop = True
    queue = []
    answer = ''
    if properString(p):
        return p
    return recursive(answer,'',p)
def recursive(answer,u,v):
    u,v = slicing(v)
    if properString(u):
        answer += u
        return recursive(answer,u,v)
    else:
        answer += '(' + recursive(answer,u,v) + ')'
        tmp = u[1:-1]
        tmp = f(tmp)
        answer += tmp
        return answer        
def slicing(string):
    u = ''
    for i in range(len(string)):
        u += string[i]
        if balancedString(u):
            return [u,string[i + 1:]]
    return ['',u]
def properString(string):
    if string == '':
        return True
    while '()' in string:
        string = string.replace('()','')
    if len(string) == 0:
        return True
    else:
        return False
def balancedString(string):
    openString = 0 
    closeString = 0
    for i in string:
        if i == '(':
            openString += 1
        else:
            closeString += 1
    if openString == closeString:
        return True
    return False
def f(string):
    result = ''
    for i in string:
        if i == ')':
            result += '('
        else:
            result += ')'
    return result
print(solution("()))((()"))
        
