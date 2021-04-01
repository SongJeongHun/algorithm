def solution():
    for i in range(int(input())):
        result_left = []
        result_right = []
        for j in list(input()):
            if j == '>':
                if result_right:
                    result_left.append(result_right.pop())
            elif j == '<':
                if result_left:
                    result_right.append(result_left.pop())
            elif j == '-':
                if result_left:
                    result_left.pop()
            else:
                result_left.append(j)
        result_left.extend(reversed(result_right))
        print(''.join(result_left))
solution()
