""" 1h 35m """
import math
def solution(progresses, speeds):
    predict = []
    answer = []
    n = (len(progresses))
    for i in range(n):
        predict.append(math.ceil((100 - progresses[i]) / speeds[i]))
    while(len(predict) > 0):
        count = 1
        element = predict.pop(0)
        predict = [i - element for i in predict]
        while(len(predict) >= 0):
            if len(predict) == 0:
                answer.append(count)
                break
            if predict[0] > 0:
                answer.append(count)
                break
            else:
                count += 1
                predict.pop(0)
    return answer
solution([93, 30, 55, 60, 40, 65], [1, 30, 5 , 10, 60, 7])
