def solution(s):
    answer = s.split(' ')
    for i in range(len(answer)):
        if answer[i] == '':
            continue
        elif answer[i][0].isalpha():
            answer[i] = answer[i][0].upper() + answer[i][1:].lower()
        else:
            if answer[i][1]:
                answer[i] = answer[i].lower()
    return ' '.join(answer)
print(solution(" f  f  f "))
