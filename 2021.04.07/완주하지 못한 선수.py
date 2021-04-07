""" 35m """
def solution(participant, completion):
    dic = dict()
    for i in participant:
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1
    for i in completion:
        dic[i] -= 1
    return dict(map(reversed,dic.items()))[1]
        
        
