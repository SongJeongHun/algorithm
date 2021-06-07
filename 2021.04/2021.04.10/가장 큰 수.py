""" 1h 5m """
def solution(numbers):
    if sum(numbers) == 0:
        return '0'
    answer = []
    numbers = sorted(list(map(str,numbers)),reverse = True,key = lambda x: x * 3)
    return ''.join(numbers)
solution([3, 30, 34, 5, 9])
