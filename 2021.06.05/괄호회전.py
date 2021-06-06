def solution(s):
    count = 0
    string = s
    for i in range(len(s)):
        if properString(string):
            count += 1
        string = string[1:] + string[0]
    return count
def properString(string):
    loop = True
    if string == '':
        return True
    while loop:
        if '()' in string:
            string = string.replace('()','')
        elif '[]' in string:
            string = string.replace('[]','')
        elif '{}' in string:
            string = string.replace('{}','')
        else:
            loop = False
    if len(string) == 0:
        return True
    else:
        return False
print(solution("[](){}"))
