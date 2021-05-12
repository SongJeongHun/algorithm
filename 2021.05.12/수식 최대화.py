import re
from itertools import permutations
def solution(expression):
    answer = []
    num = re.findall('\d+',expression)
    for i in num:
        expression = expression.replace(i,'',1)
    operator = list(expression)
    for i in list(permutations(set(operator),len(set(operator)))):
        num_tmp = num.copy()
        tmp = operator.copy()
        n = 0
        for j in i:
            while(j in tmp):
                num_index = tmp.index(j)
                n = eval(num_tmp[num_index] + j + num_tmp[num_index + 1])
                del num_tmp[num_index]
                num_tmp[num_index] = str(n)
                tmp.remove(j)
        answer.append(abs(int(num_tmp[0])))
    return max(answer)
print(solution("100-200*300-500+20"))
