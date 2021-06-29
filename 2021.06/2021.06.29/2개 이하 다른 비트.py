def solution(numbers):
    answer = []
    for i in numbers:
        target = format(i,'b')
        if i % 2 == 0:
            result = target[:-1] + '1'
            answer.append(int(result,2))
        else:
            index = target.rfind('0')
            if index == -1:
                result = "10" + target[1:]
            else:
                result = target[:index] + '10' + target[index + 2:]
            answer.append(int(result,2))
    return answer
print(solution([3,25]))
