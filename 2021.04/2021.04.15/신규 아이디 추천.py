""" 1h 39m """
def solution(new_id):
    answer = new_id
    if len(answer) == 0:
        answer += 'a'
    else:
        answer = new_id.lower()
        answer = secondStep(answer)
        answer = thirdStep(answer)
    if len(answer) >= 16:
        answer = answer[:15]
        while(answer[-1] == '.'):
            answer = answer[:-1]
    if len(answer) == 1:
        answer += answer[-1] * 2
    elif len(answer) == 2:
        answer += answer[-1]
    return answer
def secondStep(new_id):
    new = ''
    for i in new_id:
        if i.isdigit():
            new += i
            continue
        elif i.isalpha():
            new += i
            continue
        elif i == '-':
            new += i
            continue
        elif i == '_':
            new += i
            continue
        elif i == '.':
            new += i
            continue
    return new
def thirdStep(new_id):
    if len(set(new_id)) == 1 and '.' in set(new_id) or len(new_id) == 0:
        return 'a'
    new = new_id
    while('..' in new):
        new = new.replace('..','.')
    while(new[0] == '.' or new[-1] == '.'):
        if new[0] == '.':
            new = new[1:]
        if new[-1] == '.':
            new = new[:-1]
    return new
print(solution('......a......a......a.....'))
        
            
        
    
    
