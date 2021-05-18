def solution(n):
    k = n
    bag_1 = 3
    bag_2 = 5
    count = 0
    while k > 0:
        if k >= bag_2:
            k -= bag_2
            count += 1
        else:
            k -= bag_1
            count += 1
    if k < 0:
        divisor = getDivisor(n)
        if bag_2 in divisor:
            return int(n / bag_2)
        elif bag_1 in divisor:
            return int(n / bag_1)
        else:
            bag1_divisor = getDivisor(n - bag_1)
            bag2_divisor = getDivisor(n - bag_2)
            if bag_2 in bag1_divisor:
                return int((n - bag_1) / bag_2) + 1
            elif bag_2 in bag2_divisor:
                return int((n - bag_2) / bag_2) + 1
            elif bag_1 in bag1_divisor:
                return int((n - bag_1) / bag_1) + 1
            elif bag_1 in bag2_divisor:
                return int((n - bag_2) / bag_1) + 1
            else:
                return -1
    return count
def getDivisor(n):
    n = int(n)
    divisors = []
    for i in range(1, n + 1):
        if (n % i == 0):            
            divisors.append(i) 
    return divisors
print(solution(6))
print(solution(4))
print(solution(11))
print(solution(14))
print(solution(18))
print(solution(9))
print(solution(27))

