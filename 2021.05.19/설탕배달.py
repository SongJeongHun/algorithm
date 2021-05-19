def solution(n):
    bag_1 = 3
    bag_2 = 5
    count = 0
    while n >= 0:
        if n % bag_2 == 0:
            count += (n // bag_2)
            return count
        n -= bag_1
        count += 1
    else:
        return -1
print(solution(6))
print(solution(4))
print(solution(11))
print(solution(14))
print(solution(18))
print(solution(9))
print(solution(27))

