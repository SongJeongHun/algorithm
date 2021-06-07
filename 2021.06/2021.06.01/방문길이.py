def solution(dirs):
    start = [5,5]
    point = set()
    for i in dirs:
        lead = start.copy()
        if i == 'U' and start[1] + 1 <= 10:
            start[1] += 1
        elif i == 'L' and start[0] - 1 >= 0:
            start[0] -= 1
        elif i == 'R' and start[0] + 1 <= 10:
            start[0] += 1
        elif i == 'D' and start[1] - 1 >= 0:
            start[1] -= 1
        else:
            continue
        tail = start.copy()
        po = tuple(lead + tail)
        re_po = tuple(tail + lead)
        point.add(po)
        point.add(re_po)
    return len(point) // 2
print(solution("LULLLLLLU"))
