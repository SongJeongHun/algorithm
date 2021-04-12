""" 77.8 / 100.0 """
def solution(w,h):
    height = 0
    func = w / h
    for i in range(1,h):
        height += int(func * i)
    return height * 2
solution(4,3)
