def solution(p):
    return recursive('','',p,'')
def properString(string):
    if string == '':
        return ''
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
def recursive(u,v,w,result):
    if w == '':
        return ''
    for i in range(len(w)):
        u += w[i]
        if balancedString(u):
            v = w[i + 1:]
            break
    if properString(u):
        result += u
        if len(v) == 0:
            return result
        else:
            return recursive('','',v,result)
    else:
        string = recursive('','',v,'')
        new = '(' + string + ')'
        for i in u[1:-1]:
            if i == '(':
                new += ')'
            else:
                new += '('
        return result + new
print(solution("()))((()"))
