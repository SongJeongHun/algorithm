def solution(array):
    answer = []
    for i in range(len(array)):
        element = array[i]
        left = array[:i]
        right = array[i + 1:]
        answer.append(recursive(left,right,element,i,0))
    return answer
def recursive(left,right,element,i,time):
    if len(left) == 0 and len(right) == 0:
        return -1
    if len(left) == 0:
        target = right.pop(0)
        i += 1
        if target > element:
            return i
    elif len(right) == 0:
        target = left.pop()
        i -= 1
        if target > element:
            return i
    else:
        target_left = left.pop()
        target_right = right.pop(0)
        time += 1
        if target_left > element and target_right > element:
            i -= (time)
            return i
        elif target_left > element:
            i -= (time)
            return i
        elif target_right > element:
            i += (time)
            return i
    return recursive(left,right,element,i,time)

