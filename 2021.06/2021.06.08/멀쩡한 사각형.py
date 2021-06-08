from math import floor
def solution(w,h):
    if w == h:
        return w * h - w
    elif w == 1 or h == 1:
        return 0
    height = 0
    for i in range(w):
        height += floor(i * h / w)
    return height * 2
